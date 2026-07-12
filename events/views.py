from django.shortcuts import render

from .models import Event


def events(request):

    upcoming_events = Event.objects.order_by(
        "event_date"
    )

    return render(
        request,
        "events/events.html",
        {
            "events": upcoming_events
        },
    )

# Create your views here.
