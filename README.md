# Тестовое задание 1

Задание выполнено на ЯП **Python** с использованием дополнительных библиотек *(список необходимых библиотек находится в файле requirements.txt)* 
Для базы данных использовался **PostgreSQL**
Отслеживание изменение структуры БД с помощью **alembic** и библиотеки **Flask-Migrate**
Для работы web-приложения использовался фреймворк **Flask** для стилизации страниц использовался **Bootstrap**.
Онлайн документация к **API** приложения находится по адресу *[localhost:5100/apidocs](http://localhost:5100/apidocs)*

## Для работы приложения нужно:
1. Создайте виртуальное окружение и установите зависимости `pip install -r  requirements.txt`
2. Создать Базу данных в PostgreSQL 
    - После создания в файле *app/config.py* измените переменные **DB_NAME**, **DB_USER**, **DB_PASS** на название вашей БД, Имя пользователя и пароль соответственно.
    - При необходимости измените остальные параметры
3. Создать и заполнить таблицы.
    - Инициализация миграций (с помощью **Flask-Migrate**) `flask db init`
    - Создание первой миграции `flask db migrate -m 'Initialization' `
    - Обновить БД `flask db upgrade`
    - Заполнение данными `python generate_db.py`
4. Запуск приложения `python main.py`
    - Если порт занят, измените в файле *main.py* номер порта
5. Приложение готово к запуску по адресу [localhost:5100](http://localhost:5100)


## О задании

Часть 1 и Часть 2 выполненены полностью. 
