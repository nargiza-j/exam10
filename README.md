Для запуска провекта создайте виртуальное окружение

```python -m venv venv```
Далее запустите его

```venv/Scripts/activate``` или

```venv/bin/activate```
И установите библиотеки для работы приложения

```pip install -r requirements.txt```

Создание Базы данных - PostgreSQL Создайте файл .env в директории /source Далее заполните поля по примерам из .env.sample Затем примените миграции

```./manage.py migrate```

И загрузите фикстуры

```./manage.py loaddata fixtures/auth.json fixtures/dump.json```

Для запуска сервера

```./manage.py runserver```