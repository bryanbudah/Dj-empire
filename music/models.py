import os
from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Mix(models.Model):
    title = models.CharField(max_length=200)

    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE
    )

    description = models.TextField()

    cover_image = CloudinaryField(
        'image',
        folder='mix_covers/'
    )

    audio_file = CloudinaryField(
        'raw',
        folder='mixes/',
        resource_type='raw'
    )

    duration = models.CharField(
        max_length=20,
        blank=True,
        help_text="Example: 1h 15m"
    )

    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def cover_image_url(self):
        if self.cover_image:
            return self.cover_image.url
        return None

    @property
    def audio_url(self):
        if self.audio_file:
            return self.audio_file.url
        return None