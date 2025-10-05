from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, logout
from rest_framework_simplejwt.tokens import RefreshToken


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            response = redirect("post_list")

            response.set_cookie(
                "access_token",
                access_token,
                httponly=True,
                samesite="Lax",
            )
            response.set_cookie(
                "refresh_token",
                str(refresh),
                httponly=True,
                samesite="Lax",
            )

            return response
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


def logout_view(request):
    logout(request)

    response = redirect("post_list")
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")

    return response