from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import Group, User
from main.models import Experience, Organization

class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )
        self.organization = Organization.objects.create(
            name="Himpunan Mahasiswa Fasilkom",
            role="Staff Ahli",
            description="Mengembangkan program kerja keilmuan.",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, reverse("api:experience-list"))

    def test_experience_json(self):
        data = self.client.get(reverse("main:get_experience_json")).json()
        self.assertEqual(data[0]["fields"]["title"], self.experience.title)
        self.assertEqual(data[0]["fields"]["category_display"], "Part-Time")
        self.assertTrue(data[0]["fields"]["is_ongoing"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:get_experience_json"))

        self.assertEqual(response.json(), [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        data = self.client.get(reverse("main:get_experience_json")).json()

        self.assertFalse(self.experience.is_ongoing)
        self.assertFalse(data[0]["fields"]["is_ongoing"])

    def test_organization_model(self):
        self.assertEqual(str(self.organization), "Himpunan Mahasiswa Fasilkom")
        self.assertTrue(self.organization.is_ongoing)

    def test_organization_page(self):
        response = self.client.get(reverse("main:show_organization"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "organization.html")
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, reverse("api:organization-list"))
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_organization_json(self):
        data = self.client.get(reverse("main:get_organization_json")).json()
        fields = data[0]["fields"]

        self.assertEqual(fields["name"], self.organization.name)
        self.assertEqual(fields["role"], self.organization.role)
        self.assertEqual(fields["description"], self.organization.description)
        self.assertTrue(fields["is_ongoing"])

    def test_empty_organization_page(self):
        Organization.objects.all().delete()
        response = self.client.get(reverse("main:get_organization_json"))

        self.assertEqual(response.json(), [])

    def test_create_experience_ajax_access(self):
        url = reverse("main:create_experience_ajax")
        payload = {"title": "Baru", "description": "Deskripsi", "category": "internship"}

        self.assertEqual(self.client.get(url).status_code, 405)
        self.assertEqual(self.client.post(url, payload).status_code, 403)

        User.objects.create_user("biasa", password="pw12345!")
        self.client.login(username="biasa", password="pw12345!")
        self.assertEqual(self.client.post(url, payload).status_code, 403)

        User.objects.create_superuser("owner", "o@x.com", "pw12345!")
        self.client.login(username="owner", password="pw12345!")
        self.assertEqual(self.client.post(url, payload).status_code, 201)
        self.assertTrue(Experience.objects.filter(title="Baru").exists())

        bad = {**payload, "title": '<img src="x" onerror="alert(1)">'}
        self.assertEqual(self.client.post(url, bad).status_code, 400)
        self.assertEqual(Experience.objects.filter(title__icontains="img").count(), 0)

    def test_create_organization_ajax_access(self):
        url = reverse("main:create_organization_ajax")
        payload = {"name": "Org Baru", "description": "Deskripsi", "category": "volunteer"}

        self.assertEqual(self.client.get(url).status_code, 405)
        self.assertEqual(self.client.post(url, payload).status_code, 403)

        User.objects.create_superuser("owner", "o@x.com", "pw12345!")
        self.client.login(username="owner", password="pw12345!")
        self.assertEqual(self.client.post(url, payload).status_code, 201)
        self.assertTrue(Organization.objects.filter(name="Org Baru").exists())


class AjaxTest(TestCase):
    XSS = '<img src="x" onerror="alert(\'XSS!\')">'

    def setUp(self):
        self.owner = User.objects.create_superuser("owner", "o@x.com", "pw12345!")
        self.editor = User.objects.create_user("editor", password="pw12345!")
        self.editor.groups.add(Group.objects.get(name="Editor"))
        self.biasa = User.objects.create_user("biasa", password="pw12345!")

        self.exp = Experience.objects.create(
            title="Asisten Dosen PBP", description="Membantu praktikum.", category="part-time")
        self.org = Organization.objects.create(
            name="BEM Fasilkom", role="Staff", description="Divisi kominfo.")

    def test_json_star_info_for_anonymous_and_logged_in_user(self):
        self.exp.starred_by.add(self.biasa)
        self.org.starred_by.add(self.biasa, self.owner)

        anon = self.client.get(reverse("main:get_experience_json")).json()[0]["fields"]
        self.assertEqual(anon["star_count"], 1)
        self.assertFalse(anon["is_starred"])

        self.client.login(username="biasa", password="pw12345!")
        exp = self.client.get(reverse("main:get_experience_json")).json()[0]["fields"]
        org = self.client.get(reverse("main:get_organization_json")).json()[0]["fields"]
        self.assertTrue(exp["is_starred"])
        self.assertEqual(org["star_count"], 2)
        self.assertTrue(org["is_starred"])

    def test_search_filters_by_title_and_name(self):
        Experience.objects.create(title="Magang Backend", description="x")
        Organization.objects.create(name="Himpunan Mahasiswa", role="Anggota", description="x")

        res = self.client.get(reverse("main:get_experience_json"), {"title": "magang"}).json()
        self.assertEqual([i["fields"]["title"] for i in res], ["Magang Backend"])
        res = self.client.get(reverse("main:get_organization_json"), {"name": "bem"}).json()
        self.assertEqual([i["fields"]["name"] for i in res], ["BEM Fasilkom"])
        self.assertEqual(self.client.get(reverse("main:get_experience_json"), {"title": "zzz"}).json(), [])

    def test_only_owner_can_create_via_ajax(self):
        url = reverse("main:create_organization_ajax")
        payload = {"name": "Org Baru", "description": "Deskripsi", "category": "volunteer"}
        for username in (None, "biasa", "editor"):
            self.client.logout()
            if username:
                self.client.login(username=username, password="pw12345!")
            self.assertEqual(self.client.post(url, payload).status_code, 403, username)
        self.assertFalse(Organization.objects.filter(name="Org Baru").exists())

        self.client.login(username="owner", password="pw12345!")
        self.assertEqual(self.client.post(url, payload).status_code, 201)


    def test_post_without_csrf_token_is_rejected(self):
        from django.test import Client
        client = Client(enforce_csrf_checks=True)
        client.login(username="owner", password="pw12345!")
        payload = {"title": "Tanpa CSRF", "description": "x", "category": "internship"}
        self.assertEqual(client.post(reverse("main:create_experience_ajax"), payload).status_code, 403)
        self.assertFalse(Experience.objects.filter(title="Tanpa CSRF").exists())

    def test_validation_errors_return_400_with_messages(self):
        self.client.login(username="owner", password="pw12345!")
        res = self.client.post(reverse("main:create_experience_ajax"),
                                {"title": "", "description": "x", "category": "internship"})
        self.assertEqual(res.status_code, 400)
        self.assertIn("title", res.json()["errors"])

    def test_xss_payload_is_rejected_or_sanitized(self):
        self.client.login(username="owner", password="pw12345!")

        res = self.client.post(reverse("main:create_experience_ajax"),
                                {"title": self.XSS, "description": "x", "category": "internship"})
        self.assertEqual(res.status_code, 400)
        self.assertIn("Judul pengalaman", res.json()["errors"]["title"][0]["message"])

        res = self.client.post(reverse("main:create_organization_ajax"),
                                {"name": self.XSS, "role": "r", "status": "s", "description": "d"})
        self.assertEqual(res.status_code, 400)
        self.assertIn("Nama organisasi", res.json()["errors"]["name"][0]["message"])

        res = self.client.post(reverse("main:create_organization_ajax"),
                                {"name": "Org <b>Tebal</b>", "category": "volunteer",
                                "description": "Halo " + self.XSS})
        self.assertEqual(res.status_code, 201)
        saved = Organization.objects.get(name="Org Tebal")
        self.assertEqual(saved.description, "Halo")
        self.assertNotIn("<", saved.name + saved.description)