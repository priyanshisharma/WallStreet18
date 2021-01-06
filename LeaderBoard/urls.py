from django.conf.urls import url
from django.contrib.auth import login
from .views import leaderboard, leaderboard_update

urlpatterns = [
    url(r'^get/', leaderboard),
    url(r'^update/', leaderboard_update)
]