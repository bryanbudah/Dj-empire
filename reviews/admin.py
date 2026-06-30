


from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "event",
        "rating",
        "approved",
        "created_at",
    )

    list_filter = (
        "approved",
        "rating",
    )

    list_editable = (
        "approved",
    )

    search_fields = (
        "name",
        "event",
    )