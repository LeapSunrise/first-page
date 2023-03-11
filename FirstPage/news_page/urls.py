from django.urls import path
from . import views

urlpatterns = [
    path('', views.website_under_construction, name='news_page'),
]