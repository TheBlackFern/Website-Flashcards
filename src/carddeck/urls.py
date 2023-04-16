from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("new_card/", views.result, name="card_added"),
    path("delete-card/<int:card_id>/", views.delete_card, name="card_deleted"),
]