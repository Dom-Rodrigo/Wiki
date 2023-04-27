from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:query>", views.get_entry, name="get_entry")
]
