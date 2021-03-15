from django.contrib import admin
from django.urls import path
from . import views


app_name = "core"


urlpatterns = [
    path('', views.home, name="home"),
    path('index', views.index, name="index"),
    path('profile', views.profile, name="profile"),
    path('gameover', views.game_over, name="game_over"),
]
