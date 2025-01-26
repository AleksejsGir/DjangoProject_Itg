from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Используется для перенаправления

# Основные маршруты проекта
urlpatterns = [
    path('admin/', admin.site.urls),  # Административная панель
    path('news/', include('news.urls')),  # Маршруты приложения news
    path('', lambda request: redirect('news_list')),  # Перенаправление на главную страницу новостей
]
