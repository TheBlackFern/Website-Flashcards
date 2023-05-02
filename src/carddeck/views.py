import random
import json
from itertools import accumulate

from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
from .models import CardGroup, Card

def index(request):
    cards = Card.objects.all()
    amounts = [0] * 4
    for card in cards:
        if card.level <= 2:
            amounts[0] += 1
        elif 2 < card.level <= 4:
            amounts[1] += 1
        elif 4 < card.level <= 8:
            amounts[2] += 1
        else:
            amounts[3] += 1
    percentages = list(map(lambda x: x / len(cards), amounts))
    sum_percs = list(accumulate(map(lambda x: x / len(cards), amounts)))
    for_piechart = [str(int(round(n*100, 0)))+"%" for n in sum_percs]
    context = {
        "percantages_1": for_piechart[0],
        "percantages_2": for_piechart[1],
        "percantages_3": for_piechart[2],
        "perc1": str(int(round(100 * percentages[0], 0))) + "%",
        "perc2": str(int(round(100 * percentages[1], 0))) + "%",
        "perc3": str(int(round(100 * percentages[2], 0))) + "%",
        "perc4": str(int(round(100 * percentages[3], 0))) + "%",
    }
    return render(request, "pages/home.html", context)

def cards(request):
    groups = CardGroup.objects.all()
    groups_cards = [(group, reversed(group.card_set.all())) for group in groups]
    return render(request, "pages/cards.html", {"groups_cards": groups_cards})

def test(request):
    rands = [bool(random.getrandbits(1)) for _ in range(Card.objects.count())]
    cards_rand = [(model_to_dict(card), rand) for card, rand 
                  in zip(Card.objects.order_by("?"), rands)]
    js_cards_rands = json.dumps(cards_rand)
    context = {
        "cards_rand": cards_rand,
        "js_cards_rands": js_cards_rands,
    }
    return render(request, "pages/test.html", context)

def test_one(request, group_id):
    group = CardGroup.objects.get(id=group_id)
    rands = [bool(random.getrandbits(1)) for _ in range(group.card_set.all().count())]
    cards_rand = [(model_to_dict(card), rand) for card, rand 
                  in zip(group.card_set.all().order_by("?"), rands)]
    js_cards_rands = json.dumps(cards_rand)
    context = {
        "cards_rand": cards_rand,
        "js_cards_rands": js_cards_rands,
    }
    return render(request, "pages/test.html", context)

def show_groups(request):
    groups = CardGroup.objects.all()
    groups_len = [(group, group.card_set.count()) for group in groups]
    context = {
        "groups_len": groups_len,
        "compare_len_0": min(2, groups.count()),
        "compare_len_1": min(3, groups.count()),
        "compare_len_2": min(4, groups.count()),
        "compare_len_3": min(6, groups.count()),
    }
    return render(request, "pages/groups.html", context)


@csrf_exempt
def check_and_add_group(request):
    group_name = request.POST.get("group_name")
    if (not group_name):
        return JsonResponse({"valid": False})
    try:
        CardGroup.objects.create(name=group_name)
        return JsonResponse({"valid": True})
    except IntegrityError:
        return JsonResponse({"valid": False})

@csrf_exempt
def add_card(request):
    word = request.POST.get("word")
    explanation = request.POST.get("explanation")
    group_id = request.POST.get("group_id")
    group = CardGroup.objects.get(id=group_id)
    card = group.card_set.create(word=word, explanation=explanation)
    response = {'id': card.id}
    return JsonResponse(response)

@csrf_exempt
def increment_card(request, card_id):
    card = Card.objects.get(id=card_id)
    card.level += 2
    card.save()
    return JsonResponse({'status': 'ok'})

@csrf_exempt
def decrement_card(request, card_id):
    card = Card.objects.get(id=card_id)
    card.level -= 1
    card.save()
    return JsonResponse({'status': 'ok'})

@csrf_exempt
def update_card(request):
    word = request.POST.get("word")
    explanation = request.POST.get("explanation")
    card_id = request.POST.get("card_id")
    card = Card.objects.get(id=card_id)
    card.word = word
    card.explanation = explanation
    card.save()
    return JsonResponse({'status': 'ok'})

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
