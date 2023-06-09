from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from users.forms import LoginForm, SignupForm
from users.models import User


def login_view(request):
    if request.user.is_authenticated:
        return redirect("posts:feeds")

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        # # Form 클래스를 사용해 데이터를 받았다면, 반드시 is_valid()메서드를 호출해야 한다
        # print("form.is_valid():", form.is_valid())
        # # is_valid 메서드를 실행하기 전에는 cleaned_data에 접근할 수 없다
        # print("form.cleaned_data:", form.cleaned_data)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("posts:feeds")
            else:
                # print("로그인에 실패했습니다")
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다")

        context = {"form": form}
        return render(request, "users/login.html", context)
    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "users/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("users:login")


def signup(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            # username = form.cleaned_data["username"]
            # password1 = form.cleaned_data["pasword1"]
            # profile_image = form.cleaned_data["profile_image"]
            # short_description = form.cleaned_data["short_description"]
            # user = User.objects.create_user(
            #     username=username,
            #     password=password1,
            #     profile_image=profile_image,
            #     short_description=short_description,
            # )
            user = form.save()
            login(request, user)
            return redirect("posts:feeds")
    else:  # GET
        form = SignupForm()

    context = {"form": form}
    return render(request, "users/signup.html", context)