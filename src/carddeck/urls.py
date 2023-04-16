from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("new_card/", views.result, name="card_added"),
]
