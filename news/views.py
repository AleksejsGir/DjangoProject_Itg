from django.shortcuts import render, get_object_or_404
from .models import Category, News  # Импортируем модели

# Отображение всех категорий и новостей
def news_list(request):
    categories = Category.objects.all()  # Получаем все категории
    news = News.objects.all()  # Получаем все новости
    return render(request, 'news/news_list.html', {'categories': categories, 'news': news})

# Отображение новостей по категории
def news_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)  # Ищем категорию по slug
    news = News.objects.filter(category=category)  # Фильтруем новости по категории
    return render(request, 'news/news_by_category.html', {'category': category, 'news': news})

# Отображение одной новости
def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)  # Ищем новость по ID
    return render(request, 'news/news_detail.html', {'news': news_item})
