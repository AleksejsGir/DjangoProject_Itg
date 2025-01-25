# <span style="color: #3498db;">Урок 1: Введение в Django</span>

## <span style="color: #2ecc71;">Что такое Django?</span>

<span style="color: #3498db;">Django</span> — это высокоуровневый веб-фреймворк на языке <span style="color: #2ecc71;">Python</span>, который позволяет быстро и эффективно разрабатывать веб-приложения. Он следует принципу "<span style="color: #e74c3c;">Don't Repeat Yourself</span>" (DRY) и "<span style="color: #e74c3c;">Convention over Configuration</span>", что делает его очень удобным для использования. Django предоставляет множество встроенных инструментов и библиотек, которые упрощают разработку, такие как <span style="color: #f39c12;">ORM</span> (Object-Relational Mapping) для работы с базами данных, система маршрутизации (<span style="color: #f39c12;">URL routing</span>), шаблонизатор для генерации <span style="color: #f39c12;">HTML</span> и встроенная админка для управления данными.

### <span style="color: #2ecc71;">Для чего используется Django?</span>

<span style="color: #3498db;">Django</span> используется для создания веб-сайтов и веб-приложений. Он предоставляет множество встроенных инструментов и библиотек, которые упрощают разработку:

- <span style="color: #f39c12;">ORM</span> (Object-Relational Mapping): Позволяет работать с базами данных через Python-код, абстрагируясь от SQL-запросов.
- **Система маршрутизации (URL routing)**: Упрощает управление URL-адресами и их сопоставление с представлениями.
- **Шаблонизатор**: Позволяет генерировать HTML-страницы с использованием Python-кода.
- **Встроенная админка**: Предоставляет готовый интерфейс для управления данными в базе данных.

### <span style="color: #2ecc71;">Архитектура MTV</span>

<span style="color: #3498db;">Django</span> следует архитектуре <span style="color: #f39c12;">MTV</span> (Model-Template-View), которая аналогична архитектуре <span style="color: #f39c12;">MVC</span> (Model-View-Controller). Давайте разберем каждый компонент:

- **Model (Модель)**: Описывает данные и их структуру. В Django модели определяются в виде Python-классов.
- **Template (Шаблон)**: Отвечает за представление данных. Шаблоны в Django — это HTML-файлы с вставками Django-кода.
- **View (Представление)**: Обрабатывает запросы и возвращает ответы. Представления в Django — это Python-функции или классы.

#### <span style="color: #2ecc71;">Пример модели</span>

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
```

**Объяснение:**
- `Article` — это модель, которая представляет статью.
- `title` — поле для заголовка статьи, максимальная длина 200 символов.
- `content` — поле для текста статьи.
- `published_date` — поле для даты публикации статьи, автоматически устанавливается при создании записи.

#### <span style="color: #2ecc71;">Пример шаблона</span>

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ article.title }}</title>
</head>
<body>
    <h1>{{ article.title }}</h1>
    <p>{{ article.content }}</p>
</body>
</html>
```

**Объяснение:**
- `{{ article.title }}` и `{{ article.content }}` — это вставки Django, которые будут заменены значениями полей `title` и `content` модели `Article`.

#### <span style="color: #2ecc71;">Пример представления</span>

```python
from django.shortcuts import render
from .models import Article

def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'article_detail.html', {'article': article})
```

**Объяснение:**
- `article_detail` — это представление, которое принимает запрос и идентификатор статьи.
- `Article.objects.get(id=article_id)` — получает статью из базы данных по идентификатору.
- `render(request, 'article_detail.html', {'article': article})` — рендерит шаблон `article_detail.html` с переданной статьей.

## <span style="color: #2ecc71;">Создание проекта</span>

### <span style="color: #2ecc71;">Что такое Django проект?</span>

<span style="color: #3498db;">Django</span> проект — это контейнер для всех приложений и настроек, которые составляют ваше веб-приложение. Проект включает в себя конфигурационные файлы, такие как `settings.py`, `urls.py` и `wsgi.py`, а также директорию для хранения статических файлов и шаблонов. Проект служит основой для всех приложений, которые вы создаете.

### <span style="color: #2ecc71;">Создание репозитория</span>

1. **Создайте репозиторий на GitHub**:
   - Перейдите на GitHub и создайте новый репозиторий с именем `itg`.

2. **Склонируйте репозиторий на локальную машину**:
   ```sh
   git clone https://github.com/yourusername/itg.git
   cd itg
   ```

### <span style="color: #2ecc71;">Установка зависимостей</span>

1. **Создайте виртуальное окружение**:
   ```sh
   python -m venv venv
   ```

2. **Активируйте виртуальное окружение**:
   - На Linux/MacOS:
     ```sh
     source venv/bin/activate
     ```
   - На Windows:
     ```sh
     .\venv\Scripts\activate.bat
     ```

3. **Установите Django**:
   ```sh
   pip install django
   ```

4. **Сохраните зависимости в файл `requirements.txt`**:
   ```sh
   pip freeze > requirements.txt
   ```

### <span style="color: #2ecc71;">Развертывание проекта на локальной машине</span>

#### <span style="color: #2ecc71;">Через командную строку</span>

1. **Склонируйте репозиторий**:
   ```sh
   git clone https://github.com/yourusername/itg.git
   cd itg
   ```

2. **Создайте виртуальное окружение**:
   ```sh
   python -m venv venv
   ```

3. **Активируйте виртуальное окружение**:
   - На Linux/MacOS:
     ```sh
     source venv/bin/activate
     ```
   - На Windows:
     ```sh
     .\venv\Scripts\activate.bat
     ```

4. **Установите зависимости**:
   ```sh
   pip install -r requirements.txt
   ```

#### <span style="color: #2ecc71;">Через PyCharm</span>

1. **Склонируйте репозиторий**:
   - `File -> Project from Version Control -> Git`

2. **Установите зависимости**:
   - `File -> Settings -> Project Interpreter` и выберите виртуальное окружение.
   - Либо через терминал в PyCharm:
     ```sh
     pip install -r requirements.txt
     ```

### <span style="color: #2ecc71;">Создание Django проекта</span>

1. **Создайте проект**:
   ```sh
   django-admin startproject itg .
   ```

**Объяснение:**
- `django-admin startproject itg .` — создает новый проект Django с именем `itg` в текущей директории. Точка в конце команды означает, что проект будет создан в текущей директории, без создания дополнительной директории с именем проекта.

2. **Сделайте коммит**:
   ```sh
   git add .
   git commit -m "Урок 1: создаём django проект"
   ```

### <span style="color: #2ecc71;">Запуск проекта</span>

1. **Запустите сервер**:
   ```sh
   python manage.py runserver
   ```

**Объяснение:**
- `python manage.py runserver` — запускает встроенный сервер разработки Django.

2. **Остановите сервер**:
   - Используйте комбинацию клавиш `Ctrl+C`.

3. **Сделайте коммит**:
   ```sh
   git add .
   git commit -m "Урок 1: запускаем django сервер"
   ```

### <span style="color: #2ecc71;">Команды терминала</span>

- `python manage.py runserver` — запуск сервера.
- `cd` — смена директории.
- `cd ..` — переход на уровень выше.
- `ls` — просмотр содержимого директории.
- `pwd` — показать текущую директорию.

### <span style="color: #2ecc71;">Что такое Django приложение?</span>

<span style="color: #3498db;">Django</span> приложение — это модуль, который выполняет определенную функцию в вашем проекте. Приложение может включать в себя модели, представления, шаблоны и статические файлы. Приложения могут быть повторно использованы в разных проектах, что делает их модульными и гибкими.

### <span style="color: #2ecc71;">Создание приложения</span>

1. **Создайте приложение**:
   ```sh
   python manage.py startapp news
   ```

**Объяснение:**
- `python manage.py startapp news` — создает новое приложение Django с именем `news`.

2. **Зарегистрируйте приложение в `settings.py`**:
   ```python
   INSTALLED_APPS = [
       ...
       'news',
   ]
   ```

**Объяснение:**
- `INSTALLED_APPS` — список всех приложений, которые используются в проекте. Добавление `'news'` в этот список регистрирует новое приложение.

3. **Сделайте коммит**:
   ```sh
   git add .
   git commit -m "Урок 1: создаём django_app news"
   ```

### <span style="color: #2ecc71;">Создание первого представления</span>

1. **Создайте представление в `views.py`**:
   ```python
   from django.http import HttpResponse

   def main(request):
       return HttpResponse("Hello, world!")
   ```

**Объяснение:**
- `main` — это представление, которое принимает запрос и возвращает ответ.
- `HttpResponse("Hello, world!")` — создает HTTP-ответ с текстом "Hello, world!".

2. **Зарегистрируйте представление в `urls.py`**:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.main),
   ]
   ```

**Объяснение:**
- `path('', views.main)` — создает маршрут для корневого URL (`/`), который будет обрабатываться представлением `main`.

3. **Сделайте коммит**:
   ```sh
   git add .
   git commit -m "Урок 1: создаём первый маршрут и первое представление"
   ```

## <span style="color: #2ecc71;">Дополнительные знания</span>

### <span style="color: #2ecc71;">Виртуальное окружение</span>

Виртуальное окружение — это изолированная среда для <span style="color: #2ecc71;">Python</span>-проектов, которая позволяет устанавливать зависимости независимо от глобальной установки <span style="color: #2ecc71;">Python</span>. Это помогает избежать конфликтов между зависимостями разных проектов. Виртуальное окружение создается с помощью команды `python -m venv venv` и активируется с помощью команды `source venv/bin/activate` на Linux/MacOS или `.\venv\Scripts\activate.bat` на Windows.

### <span style="color: #2ecc71;">Git и GitHub</span>

<span style="color: #e74c3c;">Git</span> — это система контроля версий, которая позволяет отслеживать изменения в коде и управлять ими. <span style="color: #e74c3c;">GitHub</span> — это платформа для хостинга <span style="color: #e74c3c;">Git</span>-репозиториев, которая предоставляет удобный интерфейс для работы с <span style="color: #e74c3c;">Git</span>. <span style="color: #e74c3c;">Git</span> позволяет создавать ветки для разработки новых функций, объединять изменения из разных веток и отслеживать историю изменений.

### <span style="color: #2ecc71;">Примеры на аналогиях</span>

- **<span style="color: #3498db;">Django</span>** — это как строительная площадка, где уже есть все необходимые инструменты и материалы для постройки дома (веб-приложения).
- **Модель** — это как чертеж дома, который описывает, какие комнаты и где будут расположены.
- **Шаблон** — это как интерьер дома, который определяет, как будут выглядеть комнаты.
- **Представление** — это как менеджер строительства, который координирует работу строителей и обеспечивает, чтобы все было сделано правильно.

