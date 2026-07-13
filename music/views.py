from django.shortcuts import render
from django.db.models import Q
from .models import Mix


def mix_list(request):
    query = request.GET.get("q", "")

    mixes = Mix.objects.all()

    if query:
        mixes = mixes.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(genre__name__icontains=query)
        )

    # Top 5 most played mixes
    most_played = Mix.objects.order_by("-views")[:5]

    context = {
        "mixes": mixes,
        "query": query,
        "most_played": most_played,
    }

    return render(request, "music/mix_list.html", context)