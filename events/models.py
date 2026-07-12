
from django.db import models


class Event(models.Model):

    title = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to="events/"
    )

    venue = models.CharField(
        max_length=200
    )

    event_date = models.DateField()

    event_time = models.TimeField()

    description = models.TextField()

    ticket_price = models.CharField(
        max_length=50,
        blank=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["event_date"]

    def __str__(self):
        return self.title