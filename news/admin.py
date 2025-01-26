from django.contrib import admin
from .models import Category, News  # Импортируем модели

# Конфигурация отображения модели Category в административной панели
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')  # Поля, отображаемые в списке категорий
    list_display_links = ('id', 'name')  # Поля, превращённые в ссылки
    search_fields = ('name',)  # Поле для поиска по названию категории
    prepopulated_fields = {'slug': ('name',)}  # Автоматическое заполнение slug на основе name

# Конфигурация отображения модели News в административной панели
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at')  # Отображаемые поля в списке новостей
    list_display_links = ('id', 'title')  # Поля, превращённые в ссылки
    search_fields = ('title', 'content')  # Поля для поиска по названию и содержимому
    list_filter = ('category', 'created_at')  # Фильтры по категории и дате создания
    date_hierarchy = 'created_at'  # Навигация по иерархии дат
    ordering = ('-created_at',)  # Сортировка по дате создания (по убыванию)

# Регистрация моделей и их конфигураций в административной панели
admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
