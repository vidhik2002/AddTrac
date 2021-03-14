from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    if request.method == "POST":
        return redirect('/')

    return render(request, 'home.html', {})


def index(request):
    if request.method == "POST":
        return redirect('/index')

    return render(request, 'index.html', {})