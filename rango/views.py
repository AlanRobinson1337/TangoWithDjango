from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says hey there partner!" 
                        "<a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("This is the rango about page partner"
                        "<a href='/rango/'>Index</a>")