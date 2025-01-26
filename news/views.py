from django.shortcuts import render, get_object_or_404
from .models import News, Category

# Отображение списка новостей
def news_list(request):
    categories = Category.objects.all()
    news = News.objects.order_by('-created_at')  # Сортировка: новые записи идут первыми
    return render(request, 'news/news_list.html', {
        'categories': categories,
        'news': news
    })

# Отображение списка категорий
def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'news/categories.html', {
        'categories': categories
    })

# Отображение новостей по категории
def news_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    news = News.objects.filter(category=category).order_by('-created_at')  # Сортировка по дате создания
    return render(request, 'news/news_by_category.html', {
        'category': category,
        'news': news
    })

# Отображение подробностей новости
def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {
        'news_item': news_item
    })
