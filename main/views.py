from django.http import HttpResponse
from django.shortcuts import render

from shop.models import  Categories

def index(request):
    categories = Categories.objects.all()


    context = {
        'title': 'Главная страница',
        'content': 'Сайт медицинской диагностики - MedSite',
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': 'Тут мы рассказываем какие мы хорошие и как хорошо мы диагностируем пациентов'
    }
    return render(request, 'main/about.html', context)

def dost(request):
    context = {
        'title': 'Прием и оплата',
        'content': 'Прием и оплата',
        'text_on_page': 'Можем выехать к вам, но дорого)) Или сами приезжайте!'
    }
    return render(request, 'main/dost.html', context)


def kont(request):
    context = {
        'title': 'Контактная оплата',
        'content': 'Контактная оплата',
        'text_on_page': 'Наш телефон 8-800-800-55-35, звоните и пишите - мы есть во всех мессенджерах'
    }
    return render(request, 'main/kont.html', context)
