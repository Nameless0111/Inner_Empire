# Внутренняя Империя - Магазин Галстуков и Бабочек

Django-приложение для интернет-магазина элегантных аксессуаров.

## 🚀 Возможности

- **Каталог товаров**: Галстуки и бабочки с изображениями
- **Система ролей**: Покупатели и администраторы
- **REST API**: Полный API для интеграции
- **Пагинация**: Постраничная навигация
- **Загрузка изображений**: Поддержка медиафайлов

## 🛠 Технологии

- **Django 5.2.2**
- **Django REST Framework**
- **PostgreSQL**
- **Bootstrap 5**
- **FontAwesome**

## 📦 Установка

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/your-username/empire-shop.git
cd empire-shop
```

2. **Создайте виртуальное окружение:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Установите зависимости:**
```bash
pip install -r requirements.txt
```

4. **Настройте базу данных:**
```bash
python manage.py migrate
```

5. **Создайте суперпользователя:**
```bash
python manage.py createsuperuser
```

6. **Запустите сервер:**
```bash
python manage.py runserver
```

## 🔧 Настройка

### База данных
В `web_project/settings.py` настройте подключение к PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Медиафайлы
Создайте папку `media/` в корне проекта для загрузки изображений.

## 📚 API

### Основные эндпоинты:
- `/api/товары/` - все товары
- `/api/товары/галстуки/` - только галстуки
- `/api/товары/бабочки/` - только бабочки
- `/api/производители/` - производители
- `/api/категории/` - категории
- `/api/материалы/` - материалы

### Права доступа:
- **Чтение товаров** - доступно всем
- **Изменение товаров** - только админам
- **Пользователи** - только админам

## 👥 Роли пользователей

### Покупатель
- Просмотр товаров
- Доступ к профилю
- Нет прав на изменение

### Администратор
- Полный доступ к товарам
- Управление пользователями
- Доступ к API

## 🚀 Развертывание

### PythonAnywhere
1. Загрузите код на PythonAnywhere
2. Создайте виртуальное окружение
3. Установите зависимости: `pip install -r requirements.txt`
4. Настройте базу данных
5. Соберите статические файлы: `python manage.py collectstatic`
6. Настройте WSGI файл

## 📝 Лицензия

MIT License

## 👨‍💻 Автор

Ваше имя - [GitHub](https://github.com/your-username) 