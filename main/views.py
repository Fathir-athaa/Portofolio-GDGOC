# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, JsonResponse
import datetime
from main.models import Experience, Organization
from main.forms import ExperienceForm, OrganizationForm, ProjectForm
from django.views.decorators.http import require_POST

def is_editor_user(user):
    """True jika user login dan tergabung dalam Group 'Editor'."""
    return user.is_authenticated and user.groups.filter(name="Editor").exists()


def can_edit_data(user):
    return user.is_authenticated and (user.is_superuser or is_editor_user(user))


def can_create_or_delete_data(user):
    return user.is_authenticated and user.is_superuser

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        'name': 'Fathir Atha Rizki Tasril',
        'bio': 'Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik pada pengembangan perangkat lunak.',
        'last_login': last_login,
    }
    return render(request, 'index.html', context)

def show_experience(request):
    context = {
        'name': 'Fathir Atha Rizki Tasril',
        'form': ExperienceForm(),
        'title_query': request.GET.get("title", "").strip(),
    }
    return render(request, 'experience.html', context)


def show_organization(request):
    context = {
        'name': 'Fathir Atha Rizki Tasril',
        'form': OrganizationForm(),
        'name_query': request.GET.get("name", "").strip(),
    }
    return render(request, 'organization.html', context)

def show_project(request):
    context = {
        'name': 'Fathir Atha Rizki Tasril',
        'form': ProjectForm(),
        'title_query': request.GET.get("title", "").strip(),
    }
    return render(request, 'project.html', context)

@login_required(login_url="/login/")
def add_experience(request):
    if not can_create_or_delete_data(request.user):
        raise PermissionDenied
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('main:show_experience')
    context = {'form': form}
    return render(request, 'experience_form.html', context)

def _create_via_ajax(request, form_class, success_message):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan data."},
            status=403,
        )
    form = form_class(request.POST)
    if form.is_valid():
        obj = form.save()
        return JsonResponse({"message": success_message, "pk": str(obj.pk)}, status=201)
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


@require_POST
def create_experience_ajax(request):
    return _create_via_ajax(request, ExperienceForm, "Experience berhasil ditambahkan.")


@require_POST
def create_organization_ajax(request):
    return _create_via_ajax(request, OrganizationForm, "Organization berhasil ditambahkan.")

@login_required(login_url="/login/")
def edit_experience(request, experience_id):
    if not can_edit_data(request.user):
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience berhasil diperbarui!")
        return redirect('main:show_experience')
    context = {
        'name': 'Fathir Atha Rizki Tasril',
        'form': form,
        'experience': experience,
    }
    return render(request, 'experience_edit_form.html', context)

@login_required(login_url="/login/")
def add_organization(request):
    if not can_create_or_delete_data(request.user):
        raise PermissionDenied
    form = OrganizationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('main:show_organization')
    context = {'form': form}
    return render(request, 'organization_form.html', context)

@login_required(login_url="/login/")
def edit_organization(request, organization_id):
    if not can_edit_data(request.user):
        raise PermissionDenied
    organization = get_object_or_404(Organization, pk=organization_id)
    form = OrganizationForm(request.POST or None, instance=organization)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Organization berhasil diperbarui!")
        return redirect('main:show_organization')
    context = {
        'name': 'Fathir Atha Rizki Tasril',
        'form': form,
        'organization': organization,
    }
    return render(request, 'organization_edit_form.html', context)

def _star_data(request, obj):
    starred_users = list(obj.starred_by.all())  # sudah di-prefetch
    is_starred = request.user.is_authenticated and request.user in starred_users
    return {
        "star_count": len(starred_users),
        "is_starred": is_starred,
        "starred_by_names": ", ".join(u.username for u in starred_users),
    }

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = (
        Experience.objects.prefetch_related('starred_by', 'images')
        .order_by('-started_at')
    )
    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    data = []
    for experience in experiences:
        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.category,
                "category_display": experience.get_category_display(),
                "is_ongoing": experience.is_ongoing,
                "image_urls": [img.image.url for img in experience.images.all()],
                **_star_data(request, experience),
            },
        })
    return JsonResponse(data, safe=False)

def get_experience_xml(request):
    experiences = Experience.objects.all().order_by('-started_at')
    experience_xml = serializers.serialize("xml", experiences)
    return HttpResponse(experience_xml, content_type="application/xml")


def get_organization_json(request):
    name_query = request.GET.get("name", "").strip()
    organizations = Organization.objects.prefetch_related('starred_by', 'images').all()
    if name_query:
        organizations = organizations.filter(name__icontains=name_query)

    data = []
    for organization in organizations:
        data.append({
            "pk": str(organization.id),
            "fields": {
                "name": organization.name,
                "role": organization.role,
                "status": organization.status,
                "description": organization.description,
                "is_ongoing": organization.is_ongoing,
                "image_urls": [img.image.url for img in organization.images.all()],
                **_star_data(request, organization),
            },
        })
    return JsonResponse(data, safe=False)


def get_organization_xml(request):
    organizations = Organization.objects.all()
    organization_xml = serializers.serialize("xml", organizations)
    return HttpResponse(organization_xml, content_type="application/xml")

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not can_create_or_delete_data(request.user):
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect('main:show_experience')
    return redirect('main:show_experience')

@login_required(login_url="/login/")
def delete_organization(request, organization_id):
    if not can_create_or_delete_data(request.user):
        raise PermissionDenied
    organization = get_object_or_404(Organization, pk=organization_id)
    if request.method == "POST":
        organization.delete()
        messages.success(request, "Organization berhasil dihapus!")
        return redirect('main:show_organization')
    return redirect('main:show_organization')

@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)
        return redirect('main:show_experience')
    return redirect('main:show_experience')


@login_required(login_url="/login/")
def toggle_star_organization(request, organization_id):
    organization = get_object_or_404(Organization, pk=organization_id)
    if request.method == "POST":
        if request.user in organization.starred_by.all():
            organization.starred_by.remove(request.user)
        else:
            organization.starred_by.add(request.user)
        return redirect('main:show_organization')
    return redirect('main:show_organization')

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")
    context = {
        "name": "Fathir Atha Rizki Tasril",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response
    context = {
        "name": "Fathir Atha",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response