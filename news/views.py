from django.shortcuts import render, get_object_or_404
from .models import News, Category

# Функция отображения списка новостей
def news_list(request):
    categories = Category.objects.all()  # Получение всех категорий
    news = News.objects.order_by('-created_at')  # Сортировка новостей по дате создания (сначала новые)
    return render(request, 'news/news_list.html', {
        'categories': categories,  # Передача категорий в шаблон
        'news': news  # Передача списка новостей в шаблон
    })

# Функция отображения всех категорий
def categories_list(request):
    categories = Category.objects.all()  # Получение всех категорий
    return render(request, 'news/categories.html', {
        'categories': categories  # Передача категорий в шаблон
    })

# Функция отображения новостей по выбранной категории
def news_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)  # Получение категории по её slug или 404, если не найдена
    news = News.objects.filter(category=category).order_by('-created_at')  # Фильтрация новостей по категории
    return render(request, 'news/news_by_category.html', {
        'category': category,  # Передача информации о категории в шаблон
        'news': news  # Передача отфильтрованных новостей в шаблон
    })

# Функция отображения подробной информации о новости
def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)  # Получение новости по первичному ключу или 404
    return render(request, 'news/news_detail.html', {
        'news_item': news_item  # Передача информации о новости в шаблон
    })
