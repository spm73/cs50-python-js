from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request) -> HttpResponse:
    return render(request, "hello/index.html")


def sergio(request):
    return HttpResponse("Hello Sergio")


def greet(request, name: str) -> HttpResponse:
    return HttpResponse(f"Hello, {name.capitalize()}!")


def goodbye(request, name: str) -> HttpResponse:
    return render(request, "hello/goodbye.html", {
        "name": name.capitalize()
    })