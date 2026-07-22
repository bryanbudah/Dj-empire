from django.urls import path
from . import views

urlpatterns = [

    path(
        "register/",
        views.register,
        name="register",
    ),

    path('reset-password/', views.simple_password_reset, name='simple_password_reset'),
    path('reset-password/new/', views.set_new_password, name='set_new_password'),
    path('reset-password/success/', views.password_reset_success, name='password_reset_success'),
]