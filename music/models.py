from django.db import models


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

    cover_image = models.ImageField(
        upload_to="mixes/covers/"
    )

    audio_file = models.FileField(
        upload_to="mixes/audio/"
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
