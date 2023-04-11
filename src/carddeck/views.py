from django.shortcuts import render


def index(request):
    return render(request, "pages/main.html", {})

def result(request):
    result = request.GET["result"]
    return render(request, "pages/result.html", {"result": result})