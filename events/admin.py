

# Register your models here.
from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "venue",
        "event_date",
        "event_time",
        "ticket_price",
        "is_featured",
    )