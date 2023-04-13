from django.shortcuts import render
from .models import CardGroup

def index(request):
    groups = CardGroup.objects.all()
    groups_cards = [(group, group.card_set.all()) for group in groups]
    return render(request, "pages/main.html", {"groups_cards": groups_cards})

def result(request):
    word, explanation = request.GET["word"], request.GET["explanation"]
    return render(request, "pages/new_card.html", {"word": word, "explanation": explanation})
