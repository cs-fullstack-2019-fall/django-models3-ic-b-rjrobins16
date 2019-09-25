from django.shortcuts import render
from .models import House
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World!")


def newhouse(request):
    newhome = House(address="100 Main", bedrooms=5, bathrooms=7, squarefeet=6700.00)
    newhome.save()
    return HttpResponse('mansion saved')


def printBed(request):
    allhome = House.objects.all()
    for eachel in allhome:
        if (eachel.bedrooms > 2):
            print(eachel)
    return HttpResponse("bedrooms check")


def squarefeetchanger(request):
    allhome = House.objects.all()
    for eachel in allhome:
        if (eachel.bathrooms > 5):
            eachel.squarefeet = 9999
            print(eachel.squarefeet)
        else:
            print(eachel)
    return HttpResponse("DONE")
