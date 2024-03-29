from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_page, name='news_page'),
    path('create', views.create, name='create'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete')     # in '<int:pk>/' the "/" must have
]