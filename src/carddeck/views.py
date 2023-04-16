from django.shortcuts import render
from .models import CardGroup

def index(request):
    groups = CardGroup.objects.all()
    groups_cards = [(group, reversed(group.card_set.all())) for group in groups]
    return render(request, "pages/main.html", {"groups_cards": groups_cards})

def result(request):
    word, explanation, group_name = request.GET["word"], request.GET["explanation"], request.GET["group"]
    context = {"word": word, "explanation": explanation, "group": group_name}
    group = CardGroup.objects.get(name=group_name)
    group.card_set.create(word=word, explanation=explanation)
    return render(request, "pages/new_card.html", context)
