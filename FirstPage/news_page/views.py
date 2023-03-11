from django.shortcuts import render


def news_page(request):
    return render(request, 'news_page/news_page.html')


def website_under_construction(request):
    return render(request, 'news_page/unavailable_page.html')
