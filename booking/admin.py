from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "event_type",
        "event_date",
        "event_time",
        "location",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "event_type",
        "event_date",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
        "location",
    )
    fields = (
        "user",
        "full_name",
        "email",
        "phone",
        "event_type",
        "event_date",
        "event_time",
        "location",
        "guests",
        "message",
        "admin_notes",
        "status",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 20

    date_hierarchy = "event_date"

    actions = (
        "approve_bookings",
        "reject_bookings",
        "complete_bookings",
    )

    @admin.action(description="Approve selected bookings")
    def approve_bookings(self, request, queryset):
        queryset.update(status="Approved")

    @admin.action(description="Reject selected bookings")
    def reject_bookings(self, request, queryset):
        queryset.update(status="Rejected")

    @admin.action(description="Mark selected bookings as Completed")
    def complete_bookings(self, request, queryset):
        queryset.update(status="Completed")