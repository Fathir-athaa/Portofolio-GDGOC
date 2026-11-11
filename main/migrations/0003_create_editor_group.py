from django.db import migrations


def create_editor_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    editor_group, _ = Group.objects.get_or_create(name="Editor")

    editor_permission_codenames = [
        "change_experience",
        "change_organization",
    ]

    permissions = Permission.objects.filter(
        codename__in=editor_permission_codenames,
        content_type__app_label="main",
    )
    editor_group.permissions.set(permissions)


def remove_editor_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name="Editor").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_experience_starred_by_organization_starred_by"),
    ]

    operations = [
        migrations.RunPython(create_editor_group, remove_editor_group),
    ]