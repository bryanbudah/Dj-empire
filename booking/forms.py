from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            "full_name",
            "email",
            "phone",
            "event_type",
            "event_date",
            "event_time",
            "location",
            "guests",
            "message",
        ]

        widgets = {

            "full_name": forms.TextInput(attrs={
                "class": "w-full rounded-xl border p-3",
                "placeholder": "Full Name",
            }),

            "email": forms.EmailInput(attrs={
                "class": "w-full rounded-xl border p-3",
                "placeholder": "Email Address",
            }),

            "phone": forms.TextInput(attrs={
                "class": "w-full rounded-xl border p-3",
                "placeholder": "Phone Number",
            }),

            "event_type": forms.Select(attrs={
                "class": "w-full rounded-xl border p-3",
            }),

            "event_date": forms.DateInput(attrs={
                "type": "date",
                "class": "w-full rounded-xl border p-3",
            }),

            "event_time": forms.TimeInput(attrs={
                "type": "time",
                "class": "w-full rounded-xl border p-3",
            }),

            "location": forms.TextInput(attrs={
                "class": "w-full rounded-xl border p-3",
                "placeholder": "Event Location",
            }),

            "guests": forms.NumberInput(attrs={
                "class": "w-full rounded-xl border p-3",
                "placeholder": "Expected Guests",
            }),

            "message": forms.Textarea(attrs={
                "class": "w-full rounded-xl border p-3",
                "rows": 5,
                "placeholder": "Additional Information",
            }),

        }