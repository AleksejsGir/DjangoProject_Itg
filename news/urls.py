from django.urls import path
from . import views

# Маршруты приложения "news"
urlpatterns = [
    path('', views.news_list, name='news_list'),  # Главная страница со списком новостей
    path('categories/', views.categories_list, name='categories_list'),  # Страница со списком категорий
    path('<int:pk>/', views.news_detail, name='news_detail'),  # Страница с деталями новости
    path('category/<str:slug>/', views.news_by_category, name='news_by_category'),  # Страница новостей определённой категории
]
