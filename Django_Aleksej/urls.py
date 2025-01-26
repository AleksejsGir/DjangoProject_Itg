from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Импортируем redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),  # Все маршруты приложения news
    path('', lambda request: redirect('news_list')),  # Перенаправляем на главную страницу новостей
]
