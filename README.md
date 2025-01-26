# DjangoProject_Itg

## Описание проекта

**DjangoProject_Itg** — это новостной портал, созданный с использованием Django. Проект предназначен для публикации, категоризации и просмотра новостей по различным тематикам. Это пример приложения, где пользователи могут получить доступ к актуальным новостям и трендам.

---

## Структура проекта

```
DjangoProject_Itg/
│
├── Django_Aleksej/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── Lessons_Django/  # Папка для учебных материалов или дополнительных функций
│
├── news/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── images/
│   │       └── favicon.ico
│   ├── templates/
│   │   ├── news/
│   │   │   ├── catalog.html
│   │   │   ├── categories.html
│   │   │   ├── news_by_category.html
│   │   │   ├── news_detail.html
│   │   │   └── news_list.html
│   │   └── base.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```

---

## Основные функции проекта

1. **Категории новостей:**
   - Новости разделены на категории (например, Технология, IT-бизнес, Наука и Космос, Крипто).
   - Отображение иконок для каждой категории для улучшения визуализации.

2. **Карточки новостей:**
   - Карточки с заголовками, описаниями и изображениями (если они доступны).
   - Анимация при наведении для улучшения пользовательского опыта.

3. **Страницы:**
   - Главная страница со списком всех новостей.
   - Фильтрация новостей по категориям.
   - Детальная страница для каждой новости.

4. **Стилизация:**
   - Используются современные шрифты (например, Poppins).
   - Лёгкие анимации для кнопок категорий и карточек.
   - Адаптивный дизайн для корректного отображения на мобильных устройствах.

---

## Установка и запуск

### Требования
- Python 3.9+
- Django 4.2+

### Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/AleksejGir/DjangoProject_Itg.git
   ```

2. Перейдите в директорию проекта:
   ```bash
   cd DjangoProject_Itg
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Выполните миграции базы данных:
   ```bash
   python manage.py migrate
   ```

5. Запустите локальный сервер разработки:
   ```bash
   python manage.py runserver
   ```

6. Откройте [http://127.0.0.1:8000](http://127.0.0.1:8000) в браузере.

---

## Используемые технологии

- **Язык программирования:** Python
- **Фреймворк:** Django
- **Шрифты:** [Poppins (Google Fonts)](https://fonts.google.com/specimen/Poppins)
- **Иконки:** [Bootstrap Icons](https://icons.getbootstrap.com/)
- **Стилизация:** CSS3, Bootstrap

---

## Контакты

- Автор: Aleksej Giruckis
- GitHub: [AleksejGir](https://github.com/AleksejsGir)
- Email: aleksej.it.gir@gmail.com

---

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности смотрите в файле LICENSE.

---

## Скриншоты

![Главная страница](static/images/screenshot_main.png)

---

### Благодарности

- Команде Django за мощный фреймворк
- Сообществу Bootstrap за удобные иконки и стили
