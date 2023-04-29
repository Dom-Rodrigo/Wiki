from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new_page, name="new"),
    path("<str:query>/", views.get_entry, name="get_entry"),
    path("<str:query>/edit/", views.edit, name="edit")
]
