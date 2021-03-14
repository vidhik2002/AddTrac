
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        if None in [username, password]:
            messages.info(request, "invalid credentials")
            return redirect("login")
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/index")
        else:
            messages.info(request, "invalid credentials")
            return redirect("login")
    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if None in [first_name, last_name, username, email, password1, password2]:
            messages.info(request, "Please fill all fields")
            return redirect("register")
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, username=username, password=password1, email=email, last_name=last_name)
                user.save()
                return redirect("index")
        else:
            messages.info(request, "Password Not Matching")
            return redirect('register')
        return redirect("/")

    else:
        return render(request, 'register.html')




