from django.contrib import admin
from django.utils.html import format_html
from main.models import Experience,ExperienceImage,Organization,OrganizationImage,Project,ProjectImage

class ImageInlineBase(admin.TabularInline):
    """Kolom foto di admin: upload, pratinjau, pilihan Tampilan, dan Fokus potong."""
    fields = ('image', 'preview', 'display', 'focus')
    readonly_fields = ('preview',)
    extra = 3

    @admin.display(description="Pratinjau")
    def preview(self, obj):
        if obj and obj.image:
            return format_html('<img src="{}" style="max-height: 80px; border-radius: 6px;">', obj.image.url)
        return "-"

class ExperienceImageInline(ImageInlineBase):
    model = ExperienceImage
    extra = 35

class OrganizationImageInline(ImageInlineBase):
    model = OrganizationImage

class ProjectImageInline(ImageInlineBase):
    model = ProjectImage

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceImageInline]
    list_display = ('title', 'category', 'is_ongoing')

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [OrganizationImageInline]
    list_display = ('name', 'role', 'status', 'is_active')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('title', 'is_ongoing')