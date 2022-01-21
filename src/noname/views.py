from django.http import HttpResponse


def home_page(request):
    return HttpResponse("<h1>Quis ut Deus</1>")
