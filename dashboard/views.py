from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from booking.models import Booking


@login_required
def dashboard(request):

    bookings = Booking.objects.filter(
        user=request.user
    ).order_by("-created_at")

    total_bookings = bookings.count()

    pending_bookings = bookings.filter(
        status="Pending"
    ).count()

    approved_bookings = bookings.filter(
        status="Approved"
    ).count()

    rejected_bookings = bookings.filter(
        status="Rejected"
    ).count()

    completed_bookings = bookings.filter(
        status="Completed"
    ).count()

    context = {
        "bookings": bookings,
        "total_bookings": total_bookings,
        "pending_bookings": pending_bookings,
        "approved_bookings": approved_bookings,
        "rejected_bookings": rejected_bookings,
        "completed_bookings": completed_bookings,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )