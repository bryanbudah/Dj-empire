from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
      path(
        "password/change/",
        auth_views.PasswordChangeView.as_view(
            template_name="dashboard/change_password.html",
            success_url="/dashboard/",
        ),
        name="password_change",
    ),
]