from django.shortcuts import render


def index(request):
    return render(request, "main.html")

def result(request):
    result = request.GET["result"]
    return render(request, "result.html", {"result": result})