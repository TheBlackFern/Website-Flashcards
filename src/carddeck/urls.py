from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("new_card/", views.add_card, name="card_added"),
    path("update_card/", views.update_card, name="card_updated"),
    path("increment-card/<int:card_id>/", views.increment_card, name="card_incremented"),
    path("decrement-card/<int:card_id>/", views.decrement_card, name="card_decremented"),
    path("delete-card/<int:card_id>/", views.delete_card, name="card_deleted"),
    path("groups/", views.show_groups, name="groups"),
    path("groups/test", views.test, name="test"),
    path("groups/new_group/", views.group_added, name="group_added"),
    path("delete-group/<int:group_id>/", views.delete_group, name="group_deleted"),
]
