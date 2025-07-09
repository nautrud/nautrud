"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based viewss
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.main, name="main"),
    path("about", views.about, name="about"),
    path("works", views.works, name="works"),
    path("works/<int:work_id>/", views.work_detail, name="work_detail"),
    path("works/<int:work_id>/edit/", views.edit_work, name="edit_work"),
    path("works/<int:work_id>/delete/", views.delete_work, name="delete_work"),
    path("works/<int:work_id>/like/", views.like_work, name="like_work"),
    path(
        "collections/<int:collection_id>/",
        views.view_collection,
        name="view_collection",
    ),
    path("profile/", views.profile, name="profile"),
    path("profile/<int:user_id>/", views.profile, name="user_profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("manager/", views.manager_panel, name="manager_panel"),
    path(
        "manager/collection/create/", views.create_collection, name="create_collection"
    ),
    path(
        "manager/collection/<int:collection_id>/",
        views.manage_collection,
        name="manage_collection",
    ),
    path(
        "manager/collection/<int:collection_id>/edit/",
        views.edit_collection,
        name="edit_collection",
    ),
    path(
        "manager/work/<int:work_id>/edit/",
        views.manager_edit_work,
        name="manager_edit_work",
    ),
    path(
        "manager/work/<int:work_id>/delete/",
        views.manager_delete_work,
        name="manager_delete_work",
    ),
    path("feedback", views.feedback, name="feedback"),
    path("contacts", views.contacts, name="contacts"),
    path("login", views.user_login, name="login"),
    path("register", views.user_register, name="register"),
    path("logout", views.user_logout, name="logout"),
    path("upload", views.upload, name="upload"),
    path("faq", views.faq, name="faq"),
    path(
        "manager/feedback/<int:feedback_id>/",
        views.feedback_detail,
        name="feedback_detail",
    ),
    path("admin_panel/", views.admin_panel, name="admin_panel"),
    path(
        "admin_panel/feedback/<int:feedback_id>/",
        views.admin_feedback_detail,
        name="admin_feedback_detail",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
