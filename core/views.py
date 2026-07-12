from django.shortcuts import render

from music.models import Mix
from reviews.models import Review
from events.models import Event

def home(request):
    featured_mixes = (
        Mix.objects
        .filter(featured=True)
        .order_by("-uploaded_at")[:3]
    )

    latest_reviews = (
        Review.objects
        .filter(approved=True)
        .order_by("-created_at")[:3]
    )

    featured_event = (
        Event.objects
        .filter(is_featured=True)
        .order_by("event_date")
        .first()
    )

    context = {
        "featured_mixes": featured_mixes,
        "latest_reviews": latest_reviews,
        "featured_event": featured_event,
    }

    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def gallery(request):
    return render(request, "gallery.html")


def contact(request):
    return render(request, "contact.html")

def custom_404(request, exception):
    return render(request, "errors/404.html", status=404)


def custom_500(request):
    return render(request, "errors/500.html", status=500)