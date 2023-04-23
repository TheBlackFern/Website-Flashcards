import random

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CardGroup, Card

def index(request):
    groups = CardGroup.objects.all()
    groups_cards = [(group, reversed(group.card_set.all())) for group in groups]
    return render(request, "pages/main.html", {"groups_cards": groups_cards})

def test(request):
    cards = Card.objects.order_by("?")
    cards_rand = [(card, bool(random.getrandbits(1))) for card in cards]
    return render(request, "pages/test.html", {"cards_rand": cards_rand})

def show_groups(request):
    groups = CardGroup.objects.all()
    groups_len = [(group, len(group.card_set.all())) for group in groups]
    context = {
        "groups_len": groups_len,
        "compare_len_0": min(2, len(groups)),
        "compare_len_1": min(3, len(groups)),
        "compare_len_2": min(4, len(groups)),
        "compare_len_3": min(6, len(groups)),
    }
    return render(request, "pages/groups.html", context)

def card_added(request):
    word, explanation, group_name = request.GET["word"], request.GET["explanation"], request.GET["group"]
    context = {"word": word, "explanation": explanation, "group": group_name}
    group = CardGroup.objects.get(name=group_name)
    group.card_set.create(word=word, explanation=explanation)
    return render(request, "pages/new_card.html", context)

def group_added(request):
    group_name = request.GET["group_name"]
    context = {"group_name": group_name}
    CardGroup.objects.create(name=group_name)
    return render(request, "pages/new_group.html", context)

@csrf_exempt
def delete_card(request, card_id):
    if request.method == "POST":
        card = Card.objects.get(id=card_id)
        card.delete()
        return JsonResponse({"status": "ok"})
    else:
        return JsonResponse({"status": "error"})
    
@csrf_exempt
def delete_group(request, group_id):
    if request.method == "POST":
        group = CardGroup.objects.get(id=group_id)
        group.delete()
        return JsonResponse({"status": "ok"})
    else:
        return JsonResponse({"status": "error"})

