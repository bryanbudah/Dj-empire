from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = [
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Rejected", "Rejected"),
    ("Completed", "Completed"),
]


class Booking(models.Model):

    EVENT_CHOICES = [
        ("Wedding", "Wedding"),
        ("Club", "Club"),
        ("Birthday", "Birthday"),
        ("Corporate", "Corporate"),
        ("Festival", "Festival"),
        ("Private Party", "Private Party"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings",
        null=True,
        blank=True,
    )

    full_name = models.CharField(max_length=150)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    event_type = models.CharField(
        max_length=50,
        choices=EVENT_CHOICES,
    )

    event_date = models.DateField()

    event_time = models.TimeField()

    location = models.CharField(max_length=200)

    guests = models.PositiveIntegerField()

    message = models.TextField(
        blank=True
    )
    admin_notes = models.TextField(
    blank=True,
    help_text="Visible only to the admin. Can be shared with the customer."
)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending",
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.event_type}"