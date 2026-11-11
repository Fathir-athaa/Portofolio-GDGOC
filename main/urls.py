from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main.views import (
    show_main, show_experience, show_organization, add_experience, edit_experience,
    add_organization, edit_organization, get_experience_json, get_experience_xml,
    get_organization_json, get_organization_xml, delete_experience, delete_organization,
    register, login_user, logout_user, toggle_star_experience, toggle_star_organization,
        create_experience_ajax, create_organization_ajax, show_project,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", add_experience, name="add_experience"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path("experience/<uuid:experience_id>/edit/", edit_experience, name="edit_experience"),
    path("organization/", show_organization, name="show_organization"),
    path("organization/add/", add_organization, name="add_organization"),
    path("organization/add-ajax/", create_organization_ajax, name="create_organization_ajax"),
    path("organization/<int:organization_id>/edit/", edit_organization, name="edit_organization"),
    path("project/", show_project, name="show_project"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),

    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("api/experience/xml/", get_experience_xml, name="get_experience_xml"),
    path("api/organization/", get_organization_json, name="get_organization_json"),
    path("api/organization/xml/", get_organization_xml, name="get_organization_xml"),

    # Delete
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("organization/<int:organization_id>/delete/", delete_organization, name="delete_organization"),
        path("experience/<uuid:experience_id>/star/", toggle_star_experience, name="toggle_star_experience"),
    path("organization/<int:organization_id>/star/", toggle_star_organization, name="toggle_star_organization"),
]
if settings.DEBUG:
    # Hanya layani folder upload gambar
    urlpatterns += static("/experiences/", document_root=settings.BASE_DIR / "experiences")
    urlpatterns += static("/organization_images/", document_root=settings.BASE_DIR / "organization_images")
    urlpatterns += static("/projects/", document_root=settings.BASE_DIR / "projects")