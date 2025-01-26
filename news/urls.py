from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),  # Главная страница со списком новостей
    path('categories/', views.categories_list, name='categories_list'),  # Список категорий
    path('<int:pk>/', views.news_detail, name='news_detail'),  # Детали новости
    path('category/<str:slug>/', views.news_by_category, name='news_by_category'),  # Новости по категории
]
