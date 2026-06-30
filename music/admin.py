
from django.contrib import admin
from .models import Genre, Mix


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Mix)
class MixAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "genre",
        "featured",
        "uploaded_at",
    )

    list_filter = (
        "genre",
        "featured",
    )

    search_fields = (
        "title",
        "description",
    )