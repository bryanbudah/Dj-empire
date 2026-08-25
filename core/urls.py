from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),

  path("about/", views.about, name="about"),

    path("services/", views.services, name="services"),

    path("gallery/", views.gallery, name="gallery"),

    path("contact/", views.contact, name="contact"),

    path("robots.txt", views.robots, name="robots"),

    # ✅ Temporary — remove after use
    path("reset-password-temp/", views.reset_admin_password, name="reset_admin_password"),
] 
  