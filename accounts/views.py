from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import UsernameResetForm, SetNewPasswordForm
from django.contrib.auth.models import User
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

def simple_password_reset(request):
    form = UsernameResetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            # Store username in session
            request.session['reset_username'] = username
            return redirect('set_new_password')
    return render(request, 'registration/simple_password_reset.html', {'form': form})


def set_new_password(request):
    username = request.session.get('reset_username')
    if not username:
        return redirect('simple_password_reset')

    form = SetNewPasswordForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.get(username=username)
            user.set_password(form.cleaned_data['new_password1'])
            user.save()
            # Clear session
            del request.session['reset_username']
            return redirect('password_reset_success')

    return render(request, 'registration/set_new_password.html', {'form': form})


def password_reset_success(request):
    return render(request, 'registration/password_reset_success.html')