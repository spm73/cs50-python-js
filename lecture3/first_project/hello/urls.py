from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sergio", views.sergio, name="sergio"),
    path("<str:name>", views.goodbye, name="greet"),
]