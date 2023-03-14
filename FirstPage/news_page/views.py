from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


# DO NOT ADD "/" BEFORE NEWS_PAGE PATH

def news_page(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news_page/news_page.html', {'news': news})


def create(request):
    error = ""
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_page')
        else:
            error = 'Invalid form'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news_page/create.html', data)


def website_under_construction(request):
    return render(request, 'news_page/unavailable_page.html')
