from django.shortcuts import render
from .models import Articles


def news_page(request):
    news = Articles.objects.all()
    return render(request, 'news_page/news_page.html', {'news': news})


def website_under_construction(request):
    return render(request, 'news_page/unavailable_page.html')
