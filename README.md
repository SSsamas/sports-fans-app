# Sports Fans App (Приложение для спортивных фанатов)

Веб‑приложение на Django для спортивных фанатов. Позволяет выбрать любимые команды, тему оформления (светлая/тёмная) и язык интерфейса (EN/RU). Все настройки сохраняются в cookies и восстанавливаются при повторном заходе.

## Возможности
- Сохранение пользовательских настроек в cookies:
  - Любимые команды (список)
  - Тема интерфейса (light/dark)
  - Язык (en/ru)
  - Последняя посещённая страница
- Современный адаптивный интерфейс:
  - Карточки популярный команд
  - Боковая панель с настройками
  - Светлая/тёмная темы
- Пример данных реализован прямо в коде (списки и словари)

## Технологии
- Python 3.11+
- Django 5.2.x

## Структура проекта
```
.
├── manage.py
├── requirements.txt
├── best_practices.md
├── sports_app/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── fans/
│   ├── views.py
│   ├── models.py
│   ├── tests.py
│   ├── admin.py
│   ├── apps.py
│   └── templates/
│       └── fans/
│           └── home.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── images/
│       └── sports.jpg (добавьте файл изображения)
└── db.sqlite3 (создаётся/используется после миграций)
```

## Быстрый старт (локально)
1) Клонировать репозиторий
```bash
git clone https://github.com/SSsamas/sports-fans-app
cd sports-fans-app
```

2) Создать и активировать виртуальное окружение
- Windows
```bash
python -m venv venv
venv\Scripts\activate
```
- macOS/Linux
```bash
python -m venv venv
source venv/bin/activate
```

3) Установить зависимости
```bash
pip install -r requirements.txt
```

4) Применить миграции
```bash
python manage.py migrate
```

5) Запустить сервер разработки
```bash
python manage.py runserver
```

6) Открыть приложение в браузере
- http://127.0.0.1:8000/

## Использование
- На главной странице (/) отметьте любимые команды (чекбоксы), выберите тему и язык, затем нажмите «Сохранить».
- Настройки сохранятся в cookies и применятся автоматически при перезагрузке.
- Текущие предпочтения отображаются в правой панели (тема, язык, список избранных команд, последняя страница).

### Cookies, которые используются
- favorite_teams — массив строк с названиями команд
- theme — строка: "light" или "dark"
- language — строка: "en" или "ru"
- last_page — последняя посещённая страница (обновляется при заходе на /)

## Тестирование
Запуск стандартных тестов Django:
```bash
python manage.py test
```
(При желании можно подключить pytest и pytest-django.)

## Заметки по разработке
- Приложение `fans` зарегистрировано в `INSTALLED_APPS` (sports_app/settings.py).
- Статические файлы в dev-режиме берутся из каталога `static/`:
  ```python
  STATIC_URL = 'static/'
  STATICFILES_DIRS = [BASE_DIR / 'static']
  ```
- Если шаблон использует `{% static %}`, в начале должен быть `{% load static %}`.
- Путь к изображению по умолчанию: `static/images/sports.jpg`. Добавьте файл.
- Секреты и боевые настройки не хранить в репозитории. В проде используйте переменные окружения для `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` и настройте `STATIC_ROOT` + `collectstatic`.

## Git и публикация
1) Инициализация и первый коммит (если требуется)
```bash
git init
git add .
git commit -m "Initial commit: Django project and fans app with cookie-based preferences"
```

2) Добавление удалённого и публикация (если требуется)
```bash
git remote add origin https://github.com/SSsamas/sports-fans-app
git branch -M main
git push -u origin main
```

## Репозиторий
- GitHub: https://github.com/SSsamas/sports-fans-app

## Лицензия
MIT
