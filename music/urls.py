from django.urls import path
from . import views

urlpatterns = [
    path("", views.mix_list, name="mix_list"),
]