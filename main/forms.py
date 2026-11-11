from django.forms import ModelForm, TextInput, Textarea, Select, ChoiceField
from main.models import Experience, Organization, Project
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

# Pilihan pengganti input tanggal "Selesai Pada"
STATUS_CHOICES = [
    ("true", "Sedang berlangsung"),
    ("false", "Selesai"),
]


class StatusModelForm(ModelForm):
    """ModelForm + dropdown Status (Sedang berlangsung / Selesai)."""
    is_ongoing = ChoiceField(
        label="Status",
        choices=STATUS_CHOICES,
        required=False,
        widget=Select(attrs={"class": "form-control"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # saat edit, dropdown langsung menunjukkan status data yang sekarang
        self.fields["is_ongoing"].initial = "true" if self.instance.is_ongoing else "false"

    def save(self, commit=True):
        self.instance.is_ongoing = self.cleaned_data.get("is_ongoing") != "false"
        return super().save(commit)


class ExperienceForm(StatusModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
        ]
        labels = {
            "title": "Judul Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori",
        }
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Contoh: Software Engineer Intern",
                "maxlength": 255,
            }),
            "description": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Ceritakan pengalaman atau tanggung jawabmu...",
                "rows": 4,
            }),
            "category": Select(attrs={
                "class": "form-control",
            }),
        }

    def clean_title(self):
            title = strip_tags(self.cleaned_data["title"]).strip()
            if not title:
                raise ValidationError("Judul pengalaman tidak boleh hanya berisi tag HTML.")
            return title
    
    def clean_description(self):
            return strip_tags(self.cleaned_data["description"]).strip()

class OrganizationForm(StatusModelForm):
    class Meta:
        model = Organization
        fields = [
            "name",
            "description",
            "category",
        ]
        labels = {
            "name": "Nama Organisasi",
            "description": "Deskripsi Organisasi",
            "category": "Kategori",
        }
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Contoh: BEM Fasilkom UI",
                "maxlength": 200,
            }),
            "description": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Ceritakan kegiatan atau tanggung jawabmu di organisasi ini...",
                "rows": 4,
            }),
            "category": Select(attrs={
                "class": "form-control",
            }),
        }

    def clean_name(self):
        name = strip_tags(self.cleaned_data["name"]).strip()
        if not name:
            raise ValidationError("Nama organisasi tidak boleh hanya berisi tag HTML.")
        return name

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()


class ProjectForm(StatusModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
        ]
        labels = {
            "title": "Judul Project",
            "description": "Deskripsi Project",
        }
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Contoh: Website Portofolio Django",
                "maxlength": 255,
            }),
            "description": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Ceritakan project ini dan peranmu di dalamnya...",
                "rows": 4,
            }),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Judul project tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()