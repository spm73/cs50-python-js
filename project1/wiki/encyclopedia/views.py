from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponse #, HttpResponseRedirect
from django.urls import reverse

from . import util
from markdown2 import Markdown
from random import choice


def index(request) -> HttpResponse:
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title: str) -> HttpResponse:
    content = util.get_entry(title)
    if content is None:
        return HttpResponseNotFound(f"There is no entry for {title}")
    
    return HttpResponse(Markdown().convert(content))


def new(request) -> HttpResponse:
    return HttpResponse("Create a new page")


def random_page(request) -> HttpResponse:
    # return HttpResponseRedirect(reverse("encyclopedia:entry", args=[choice(util.list_entries())]))
    return redirect(reverse("encyclopedia:entry", args=[choice(util.list_entries())]))


def search(request) -> HttpResponse:
    if request.method != "POST":
        return redirect(reverse("encyclopedia:index"))
        
    entry_title = request.POST["q"]
    if entry_title in util.list_entries():
        return redirect(reverse("encyclopedia:entry", args=[entry_title]))
    else:
        return render(request, 'encyclopedia/search_error.html', {
            "entries": util.list_entries(),
            "entry_title": entry_title
        })