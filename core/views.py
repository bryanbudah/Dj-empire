from django.shortcuts import render

from music.models import Mix
from reviews.models import Review
from events.models import Event
from django.db.models import Q
from django.http import HttpResponse

def mix_list(request):
    query = request.GET.get("q", "")

    mixes = Mix.objects.all()

    if query:
        mixes = mixes.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(genre__name__icontains=query)
        )

    most_played = Mix.objects.order_by("-views")[:5]

    context = {
        "mixes": mixes,
        "query": query,
        "most_played": most_played,
    }

    return render(request, "music/mix_list.html", context)

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

def robots(request):
    return HttpResponse(
        open("templates/robots.txt").read(),
        content_type="text/plain"
    )