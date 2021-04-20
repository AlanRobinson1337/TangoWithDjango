from django.shortcuts import render
from django.template import loader

from .models import News
from django.http import HttpResponse
from datetime import date
from rango import models

def index(request):
    news_list = News.objects.order_by('Headline')[:5]
    template = loader.get_template('rango/index.html')
    context = {
        'news_list': news_list,
    }
    return render(request, 'rango/index.html', context)


