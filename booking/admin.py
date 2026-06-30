from django.contrib import admin

# Register your models here.
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "event_type",
        "event_date",
        "status",
    )

    list_filter = (
        "status",
        "event_type",
    )

    search_fields = (
        "full_name",
        "email",
    )