from django.urls import path

from . import views

urlpatterns = [

    path("", views.booking, name="booking"),

    path(
        "success/",
        views.booking_success,
        name="booking_success",
    ),
     path(
        "<int:booking_id>/",
        views.booking_detail,
        name="booking_detail",
    ),
path("<int:booking_id>/", views.booking_detail, name="booking_detail"),
]