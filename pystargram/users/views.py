from django.shortcuts import render, redirect


# Create your views here.
from users.forms import LoginForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/posts/feeds/")

    form = LoginForm()

    context = {
        "form": form,
    }

    return render(request, "users/login.html", context)