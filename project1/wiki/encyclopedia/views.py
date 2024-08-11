from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse

from . import util
from markdown2 import Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title: str) -> HttpResponse:
    content = util.get_entry(title)
    if content is None:
        return HttpResponseNotFound(f"There is no entry for {title}")
    
    return HttpResponse(Markdown().convert(content))