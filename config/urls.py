from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
    path("mixes/", include("music.urls")),
    path("booking/", include("booking.urls")),
    path("accounts/", include("accounts.urls")),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path("dashboard/", include("dashboard.urls")),
    path("reviews/", include("reviews.urls")),
    path("events/", include("events.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),

  

# Add these inside urlpatterns:
path(
    "accounts/password-reset/",
    auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset.html",
        email_template_name="registration/password_reset_email.html",
        subject_template_name="registration/password_reset_subject.txt",
        success_url="/accounts/password-reset/done/"
    ),
    name="password_reset",
),
path(
    "accounts/password-reset/done/",
    auth_views.PasswordResetDoneView.as_view(
        template_name="registration/password_reset_done.html"
    ),
    name="password_reset_done",
),
path(
    "accounts/password-reset-confirm/<uidb64>/<token>/",
    auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/password_reset_confirm.html",
        success_url="/accounts/password-reset-complete/"
    ),
    name="password_reset_confirm",
),
path(
    "accounts/password-reset-complete/",
    auth_views.PasswordResetCompleteView.as_view(
        template_name="registration/password_reset_complete.html"
    ),
    name="password_reset_complete",
),
]

handler404 = "core.views.custom_404"
handler500 = "core.views.custom_500"