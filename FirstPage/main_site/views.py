from django.shortcuts import render, redirect


def index(request):
    data = {
        'title': 'Main page!!!!',
        'values': ['Shalom', 'Hellol World', '1488/228'],
        'obj': {
            'car': 'AUDI',
            'age': 22,
            'hobby': 'Srunk'
        }
    }
    return render(request, 'main_site/index.html', data)

def about(request):
    return render(request, 'main_site/about.html')

def contacts(request):
    return render(request, 'main_site/unavailable_page.html')

def website_under_construction(request):
    return render(request, 'main_site/unavailable_page.html')