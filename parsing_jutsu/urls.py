from django.urls import path
from . import views

urlpatterns = [
    path("jutsu_list/", views.JutsuListView.as_view(), name="jutsu_list"),
    path("jutsu_parser/", views.JutsuFormView.as_view(), name="jutsu_parser"),
]
