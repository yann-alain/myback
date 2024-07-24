from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="polls-home"),
    path("about/", views.about, name="polls-about"),
]