from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("cards/", views.cards, name="cards"),
    path("new_card/", views.add_card, name="card_added"),
    path("update_card/", views.update_card, name="card_updated"),
    path("increment-card/<int:card_id>/", views.increment_card, name="card_incremented"),
    path("decrement-card/<int:card_id>/", views.decrement_card, name="card_decremented"),
    path("delete-card/<int:card_id>/", views.delete_card, name="card_deleted"),
    path("test", views.test, name="test"),
    path("test/<int:group_id>", views.test_one, name="test_one"),
    path("groups/", views.show_groups, name="groups"),
    path("new_group/", views.check_and_add_group),
    path("delete-group/<int:group_id>/", views.delete_group, name="group_deleted"),
]
