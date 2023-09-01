from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages

from .forms import MyUserCreationForm


# Create your views here.
def register(request: HttpRequest):
    if request.method == "POST":
        reg_form = MyUserCreationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(
                request, "New User Account Created! Login to get started..."
            )
            return redirect("register")
    else:
        reg_form = MyUserCreationForm()
    return render(request, "register.html", {"reg_form": reg_form})
