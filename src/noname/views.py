from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, "index.html")


def about_page(request):
    return HttpResponse("<h1>About</1>")


def content_page(request):
    return HttpResponse("<h1>Content</1>")
