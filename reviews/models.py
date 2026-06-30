from django.db import models


class Review(models.Model):

    RATING_CHOICES = [
        (5, "★★★★★"),
        (4, "★★★★☆"),
        (3, "★★★☆☆"),
        (2, "★★☆☆☆"),
        (1, "★☆☆☆☆"),
    ]

    name = models.CharField(max_length=120)

    event = models.CharField(max_length=150)

    comment = models.TextField()

    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=5,
    )

    image = models.ImageField(
        upload_to="reviews/",
        blank=True,
        null=True,
    )

    approved = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.name} ({self.rating}★)"