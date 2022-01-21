from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    my_title = "Help Desk Blog"
    return render(request, "index.html", {"title": my_title})


def about_page(request):
    return render(request, "about.html", {"title": "About"})


def contact_page(request):
    return render(request, "index.html", {"title": "Contact us"})
