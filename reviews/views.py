from django.shortcuts import render


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from booking.models import Booking
from .forms import ReviewForm
from .models import Review


@login_required
def create_review(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user,
    )

    if booking.status != "Completed":
        messages.error(
            request,
            "You can only review completed bookings."
        )
        return redirect("dashboard")

    if hasattr(booking, "review"):
        messages.warning(
            request,
            "You have already reviewed this booking."
        )
        return redirect("booking_detail", booking.id)

    if request.method == "POST":

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)

            review.user = request.user
            review.booking = booking

            review.save()

            messages.success(
                request,
                "Thank you! Your review has been submitted for approval."
            )

            return redirect("booking_detail", booking.id)

    else:

        form = ReviewForm()

    return render(
        request,
        "reviews/create_review.html",
        {
            "form": form,
            "booking": booking,
        },
    )
def testimonials(request):

    reviews = Review.objects.filter(
        approved=True
    ).select_related(
        "booking",
        "user"
    )

    return render(
        request,
        "reviews/testimonials.html",
        {
            "reviews": reviews,
        },
    )