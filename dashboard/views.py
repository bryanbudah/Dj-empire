from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from booking.models import Booking
from .forms import UserUpdateForm


@login_required
def dashboard(request):

    bookings = Booking.objects.filter(
        user=request.user
    ).order_by("-created_at")

    context = {
        "bookings": bookings,
        "total_bookings": bookings.count(),
        "pending_bookings": bookings.filter(status="Pending").count(),
        "approved_bookings": bookings.filter(status="Approved").count(),
        "rejected_bookings": bookings.filter(status="Rejected").count(),
        "completed_bookings": bookings.filter(status="Completed").count(),
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )


@login_required
def edit_profile(request):

    if request.method == "POST":

        form = UserUpdateForm(
            request.POST,
            instance=request.user,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Your profile has been updated successfully!"
            )

            return redirect("dashboard")

    else:

        form = UserUpdateForm(
            instance=request.user,
        )

    return render(
        request,
        "dashboard/edit_profile.html",
        {
            "form": form,
        },
    )