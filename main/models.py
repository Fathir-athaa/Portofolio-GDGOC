import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class ImageDisplayMixin(models.Model):
    """Pengaturan tampilan foto di kartu (dipakai foto Experience, Organization, Project)."""
    DISPLAY_CHOICES = [
        ('auto', 'Asli (ikuti bentuk foto)'),
        ('16/9', 'Landscape 16:9'),
        ('4/3', 'Landscape 4:3'),
        ('1/1', 'Persegi 1:1'),
        ('3/4', 'Portrait 3:4'),
        ('9/16', 'Portrait 9:16'),
    ]
    FOCUS_CHOICES = [
        ('center', 'Tengah'),
        ('top', 'Atas'),
        ('bottom', 'Bawah'),
        ('left', 'Kiri'),
        ('right', 'Kanan'),
    ]

    display = models.CharField("Tampilan", max_length=10, choices=DISPLAY_CHOICES, default='auto')
    focus = models.CharField(
        "Fokus potong", max_length=10, choices=FOCUS_CHOICES, default='center',
        help_text="Bagian foto yang dipertahankan saat foto dipotong (tidak berlaku untuk tampilan Asli).",
    )

    class Meta:
        abstract = True

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    starred_by = models.ManyToManyField(User, related_name="starred_experiences", blank=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None
    
    @is_ongoing.setter
    def is_ongoing(self, value):
        # dipanggil saat user memilih Status di form
        if value:
            self.ended_at = None              # Sedang berlangsung
        elif self.ended_at is None:
            self.ended_at = timezone.now()    # Selesai -> catat waktu sekarang
    

class ExperienceImage(ImageDisplayMixin):
    experience = models.ForeignKey(Experience, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='experiences/gallery/')

    def __str__(self):
        return f"Foto untuk {self.experience.title}"

class Organization(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=Experience.EXPERIENCE_CHOICES, default='full-time')
    ended_at = models.DateTimeField(blank=True, null=True)
    # field lama: tidak dipakai lagi di form, tapi tetap disimpan supaya data lama tidak hilang
    role = models.CharField(max_length=100, blank=True, default="")
    status = models.CharField(max_length=50, default="Active Member")
    is_active = models.BooleanField(default=True)
    starred_by = models.ManyToManyField(User, related_name="starred_organizations", blank=True)

    def __str__(self):
        return self.name
    
    @property
    def is_ongoing(self):
        return self.ended_at is None
    
    @is_ongoing.setter
    def is_ongoing(self, value):
        # dipanggil saat user memilih Status di form
        if value:
            self.ended_at = None              # Sedang berlangsung
        elif self.ended_at is None:
            self.ended_at = timezone.now()    # Selesai -> catat waktu sekarang

class OrganizationImage(ImageDisplayMixin):
    organization = models.ForeignKey(Organization, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='organization_images/')

    def __str__(self):
        return f"Image for {self.organization.name}"


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    starred_by = models.ManyToManyField(User, related_name="starred_projects", blank=True)

    def __str__(self):
        return self.title

    @property
    def is_ongoing(self):
        return self.ended_at is None

    @is_ongoing.setter
    def is_ongoing(self, value):
        # dipanggil saat user memilih Status di form
        if value:
            self.ended_at = None              # Sedang berlangsung
        elif self.ended_at is None:
            self.ended_at = timezone.now()    # Selesai -> catat waktu sekarang

class ProjectImage(ImageDisplayMixin):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')

    def __str__(self):
        return f"Foto untuk {self.project.title}"