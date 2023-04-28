from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:query>", views.get_entry, name="get_entry"),
    path("new/", views.new_page, name="new")
]
