from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:TITLE>", views.title, name="title"),
    path("search", views.search, name="search"),
    path("createNewPage", views.createNewPage, name="createNewPage"),
    path("editPage/<str:newTitle>", views.editPage, name="editPage"),
    path("randomPage", views.randomPage, name="randomPage")
]
