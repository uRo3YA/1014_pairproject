from django.shortcuts import render, redirect

# from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def index(request):
    users = User.objects.all()
    # Template에 전달한다.
    context = {"users": users}
    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)
