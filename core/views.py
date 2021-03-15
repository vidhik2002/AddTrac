from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required()
def home(request):
	print("home")
	return render(request, 'home.html', {})


def index(request):
    if request.method == "POST":
        return redirect('/index')

    return render(request, 'index.html', {})


def profile(request):
    if request.method == "POST":
        return redirect("/profile")

    return render(request, 'profile.html', {})


def game_over(request):
    if request.method == "POST":
        return redirect('/gameover')

    return render(request, 'game_over.html', {})