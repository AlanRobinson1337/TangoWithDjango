from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    #return HttpResponse("Rango says hey there partner!"  "<a href='/rango/about/'>About</a>")
    context_dict = {'boldmessage': 'Cruncy, creamy, cooking, andy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("This is the rango about page partner"
                        "<a href='/rango/'>Index</a>")
