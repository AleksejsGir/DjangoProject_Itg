
# 🌐 **Info to Go**
Добро пожаловать на новостной портал **Info to Go** — ваш надёжный источник актуальных новостей! 🎉


## Описание проекта


## 🖥️ **Описание проекта**
Info to Go — это Django-проект, предоставляющий удобный и современный интерфейс для просмотра новостей по категориям. Благодаря адаптивному дизайну, платформа доступна как на настольных компьютерах, так и на мобильных устройствах.

### 📋 **Ключевые функции**
- 🔍 **Поиск по новостям:** Легко находите интересующие статьи.
- 📂 **Категории новостей:**
  - Технологии 💻
  - Наука и космос 🚀
  - Криптовалюты 💰
  - IT-бизнес 📊
- 📰 **Детализированные страницы новостей:** Содержимое статей с датой публикации.
- 🌟 **Элегантный дизайн:** Простота использования с поддержкой тёмной темы.

---


```
DjangoProject_Itg/
│
├── Django_Aleksej/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── news/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── static/
│   │   ├── css/
│   │   │   ├── styles.css
│   │   ├── images/
│   ├── templates/
│   │   ├── news/
│   │   │   ├── catalog.html
│   │   │   ├── categories.html
│   │   │   ├── news_by_category.html
│   │   │   ├── news_detail.html
│   │   │   ├── news_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── templates/
│   ├── base.html
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
├── requirements.txt
```

---

## 📦 **Установка проекта**

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/AleksejGir/DjangoProject_Itg.git
   ```

2. Перейдите в директорию проекта:
   ```bash
   cd DjangoProject_Itg
   ```

2. **Создайте виртуальное окружение и активируйте его**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   ```

3. **Установите зависимости**
   ```bash
   pip install -r requirements.txt
   ```

4. **Примените миграции базы данных**
   ```bash
   python manage.py migrate
   ```

5. **Запустите локальный сервер**
   ```bash
   python manage.py runserver
   ```
   Откройте [http://127.0.0.1:8000](http://127.0.0.1:8000) в вашем браузере.

6. Откройте [http://127.0.0.1:8000](http://127.0.0.1:8000) в браузере.

---

## 🎨 **Технические особенности**
- **Фронтенд:** Bootstrap 5 и кастомный CSS.
- **Бэкенд:** Django с ORM для работы с базой данных.
- **База данных:** SQLite (можно заменить на PostgreSQL).
- **Адаптивность:** Полностью поддерживает мобильные устройства.

---

## 🖼️ **Пример интерфейса**
!![Пример интерфейса](screenshots/screenshot.png)

---

## 🛠️ **Разработка и тестирование**

### 🧪 **Тестирование**
1. Запустите тесты:
   ```bash
   python manage.py test
   ```
2. Добавьте больше тестов в `news/tests.py` для покрытия бизнес-логики.

### 📖 **Документация**
- Комментарии добавлены в каждом ключевом файле для упрощения поддержки.
- Подробнее смотрите в коде:
  - `views.py`: Логика отображения.
  - `models.py`: Структура данных.

---

## 👥 **Контрибьюторы**
- Aleksej — разработчик и дизайнер проекта.

---

## 📩 **Контакты**
✉️ Email: aleksej.it.gir@gmail.com  
🔗 GitHub: [AleksejsGir](https://github.com/AleksejsGir)
