from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.
def index(request) -> HttpResponse:
    now = datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })