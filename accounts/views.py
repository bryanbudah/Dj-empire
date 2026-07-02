from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegisterForm


def register(request):
    """
    Register a new user account.
    """

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "🎉 Your account has been created successfully! Please log in."
            )

            return redirect("login")

        messages.error(
            request,
            "Please correct the errors below."
        )

    else:
        form = RegisterForm()

    return render(
        request,
        "registration/register.html",
        {
            "form": form,
        },
    )