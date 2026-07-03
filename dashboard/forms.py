from django import forms
from django.contrib.auth.models import User


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            "first_name",
            "last_name",
            "email",
        ]

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "w-full border rounded-lg p-3"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "w-full border rounded-lg p-3"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "w-full border rounded-lg p-3"
                }
            ),
        }