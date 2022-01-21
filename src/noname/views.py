from django.http import HttpResponse


def home_page(request):
    return HttpResponse("<h1>Help Desk Blog</1>")


def about_page(request):
    return HttpResponse("<h1>About</1>")


def content_page(request):
    return HttpResponse("<h1>Content</1>")
