from django.db import models

# Create your models here.

class Booking(models.Model):

    EVENT_CHOICES = [

        ("Wedding", "Wedding"),
        ("Club", "Club"),
        ("Birthday", "Birthday"),
        ("Corporate", "Corporate"),
        ("Festival", "Festival"),
        ("Private Party", "Private Party"),

    ]

    STATUS_CHOICES = [

        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),

    ]

    full_name = models.CharField(max_length=150)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    event_type = models.CharField(
        max_length=50,
        choices=EVENT_CHOICES
    )

    event_date = models.DateField()

    event_time = models.TimeField()

    location = models.CharField(max_length=200)

    guests = models.PositiveIntegerField()

    message = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ["-created_at"]

    def __str__(self):

        return f"{self.full_name} - {self.event_type}"