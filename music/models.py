
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Mix(models.Model):
    title = models.CharField(max_length=200)

    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name="mixes"
    )

    description = models.TextField()

    cover_image = models.ImageField(
        upload_to="mix_covers/"
    )

    audio_file = models.FileField(
        upload_to="mixes/"
    )

    duration = models.CharField(
        max_length=20,
        blank=True
    )

    featured = models.BooleanField(
        default=False
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title