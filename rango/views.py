from django.shortcuts import render
from rango.models import Category
from django.http import HttpResponse


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    return render(request, 'rango/index.html', context=context_dict)
    #return HttpResponse("Rango says hey there partner!"  "<a href='/rango/about/'>About</a>")
    #context_dict = {'boldmessage': 'Cruncy, creamy, cooking, andy, cupcake!'}
    #return render(request, 'rango/index.html', context=context_dict)

#def about(request):
#    return HttpResponse("This is the rango about page partner"
#                        "<a href='/rango/'>Index</a>")

def about(request):
    return render(request, 'rango/about.html')