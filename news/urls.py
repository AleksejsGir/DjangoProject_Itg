from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),  # Главная страница с новостями
    path('category/<slug:slug>/', views.news_by_category, name='news_by_category'),  # Новости по категории
    path('<int:news_id>/', views.news_detail, name='news_detail'),  # Детальная страница новости
]
