

from django.shortcuts import render
from .models import Mix

def mix_list(request):
    mixes = Mix.objects.all().order_by("-uploaded_at")

    return render(request, "music/mix_list.html", {
        "mixes": mixes,
    })