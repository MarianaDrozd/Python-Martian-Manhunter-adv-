from random import randint
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def status_view(request):
    return HttpResponse("Super good!")


def random_color(request):
    return HttpResponse("#" + "%06x" % randint(0, 0xFFFFFF))
