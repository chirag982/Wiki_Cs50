from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("add/", views.create_entry, name="create_entry"),
    path("edit", views.edit_entry, name="edit_entry"),
    path("edited", views.edit, name="edited"),
    path("random", views.random_entry, name="random")
]
