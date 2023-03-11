from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('about', views.about, name='aboutpage'),
    path('contacts', views.contacts, name='contactspage'),
    path('unavailable_page', views.website_under_construction, name='unavailable_page')
]