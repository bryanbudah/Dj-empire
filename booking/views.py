from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookingForm
from .models import Booking


def booking(request):

    if request.method == "POST":

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            if request.user.is_authenticated:
                booking.user = request.user

            booking.save()

            return redirect("booking_success")

    else:
        form = BookingForm()

    return render(
        request,
        "booking/booking_form.html",
        {
            "form": form,
        },
    )


def booking_success(request):

    return render(
        request,
        "booking/booking_success.html",
    )


@login_required
def booking_detail(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user,
    )

    return render(
        request,
        "booking/booking_detail.html",
        {
            "booking": booking,
        },
    )