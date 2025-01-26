from django.db import models

# Модель для категорий новостей
class Category(models.Model):
    name = models.CharField(
        max_length=100,  # Максимальная длина строки - 100 символов
        unique=True,  # Уникальность названия категории
        verbose_name="Название категории"  # Название поля для отображения в админке
    )
    slug = models.SlugField(
        unique=True,  # Уникальный URL для категории
        verbose_name="URL категории"  # Отображаемое имя поля в админке
    )

    class Meta:
        verbose_name = "Категория"  # Имя модели в единственном числе в админке
        verbose_name_plural = "Категории"  # Имя модели во множественном числе

    def __str__(self):
        return self.name  # Отображение объекта в виде названия категории


# Модель для новостей
class News(models.Model):
    title = models.CharField(
        max_length=200,  # Максимальная длина строки - 200 символов
        verbose_name="Заголовок новости"  # Название поля для отображения в админке
    )
    content = models.TextField(
        verbose_name="Содержимое новости"  # Текстовое содержимое новости
    )
    category = models.ForeignKey(
        Category,  # Связь с моделью Category
        on_delete=models.CASCADE,  # При удалении категории удаляются связанные новости
        related_name="news",  # Имя обратной связи (Category.news)
        verbose_name="Категория"  # Отображаемое имя поля в админке
    )
    created_at = models.DateTimeField(
        auto_now_add=True,  # Устанавливается автоматически при создании записи
        verbose_name="Дата создания"  # Имя поля для отображения в админке
    )
    updated_at = models.DateTimeField(
        auto_now=True,  # Обновляется автоматически при сохранении записи
        verbose_name="Дата обновления"  # Имя поля для отображения в админке
    )

    class Meta:
        verbose_name = "Новость"  # Имя модели в единственном числе
        verbose_name_plural = "Новости"  # Имя модели во множественном числе
        ordering = ["-created_at"]  # Сортировка по дате создания (новые сверху)

    def __str__(self):
        return self.title  # Отображение объекта в виде заголовка новости
