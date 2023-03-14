from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm
# DO NOT ADD "/" BEFORE NEWS_PAGE PATH

def news_page(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news_page/news_page.html', {'news': news})


def create(request):
    form = ArticlesForm()

    data = {
        'form': form
    }

    return render(request, 'news_page/create.html', data)


def website_under_construction(request):
    return render(request, 'news_page/unavailable_page.html')
