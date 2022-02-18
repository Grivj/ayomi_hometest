from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .forms import UpdateEmailForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/profile/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request):
    if request.is_ajax():
        form = UpdateEmailForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            new_email = form.cleaned_data.get("email")
            return JsonResponse(
                {
                    "type": "success",
                    "updated_email": new_email,
                    "alert": f'Your email has been updated to "{new_email}"',
                }
            )
        return JsonResponse(
            {
                "type": "danger",
                "alert": "An error occured while updating your email. Please enter a valid email address.",
            }
        )
    else:
        form = UpdateEmailForm(instance=request.user)
        user = request.user
        context = {
            "username": user.username,
            "email": user.email or "Undefined",
            "form": form,
        }
    return render(request, "profile.html", context=context)
