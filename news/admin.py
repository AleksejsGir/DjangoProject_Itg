from django.contrib import admin
from .models import Category, News  # Импортируем модели

# Настраиваем отображение модели Category в админке
class CategoryAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке категорий
    list_display = ('id', 'name', 'slug')  # Поля: ID, название, slug
    list_display_links = ('id', 'name')  # Поля, которые являются ссылками
    search_fields = ('name',)  # Поля для поиска
    prepopulated_fields = {'slug': ('name',)}  # Автозаполнение slug из названия

# Настраиваем отображение модели News в админке
class NewsAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке новостей
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')  # Поля, которые являются ссылками
    search_fields = ('title', 'content')  # Поля для поиска
    list_filter = ('category', 'created_at')  # Фильтры по категории и дате
    date_hierarchy = 'created_at'  # Иерархия по дате создания
    ordering = ('-created_at',)  # Сортировка по дате создания (от новых к старым)

# Регистрируем модели и их настройки в админке
admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
