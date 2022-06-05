from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path("auth/", include("rest_auth.urls")),
    path("hello/", views.HelloView.as_view(), name="hello"),
]
