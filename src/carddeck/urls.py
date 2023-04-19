from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("new_card/", views.card_added, name="card_added"),
    path("groups/new_group/", views.group_added, name="group_added"),
    path("groups/", views.show_groups, name="groups"),
    path("delete-card/<int:card_id>/", views.delete_card, name="card_deleted"),
    path("delete-group/<int:group_id>/", views.delete_group, name="group_deleted"),
]