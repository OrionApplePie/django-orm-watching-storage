# Веб-приложение пульт охраны хранилища банка

Приложения для учета посещений сотрудниками хранилища банка.
В базе данных ведется учет пропусков и фиксируются все посещения. Приложение позволяет охраннику отслеживать всех кто находится внутри хранилища, а также выявлять подозрительные посещения.

## Требования

Должно быть установлены следующее ПО:

- [Python 3.x](https://www.python.org/)
- [Git](https://git-scm.com/download)

Для Windows можно использовать:

- [GitHub Desktop](https://desktop.github.com/) &mdash; gui для git.
- [Cmdr](https://cmder.net/) &mdash; удобная замена стандартной командной строке Windows.


## Как установить

Скопируйте ссылку на репозиторий:
```
https://github.com/OrionApplePie/django-orm-watching-storage.git
```

В терминале выполните команду:
```
git clone https://github.com/OrionApplePie/django-orm-watching-storage.git
```
после чего репозиторий скачается и будет доступен локально.

Далее перейдите в папку с репозиторием, и используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Создайте файл .env в корне проекта. Внесите следующие данные:
```
CHECKPOINT_DB_HOST=<адрес_базы_данных>
CHECKPOINT_DB_PORT=<порт_базы_данных>
CHECKPOINT_DB_NAME=<имя_базы_данных>
CHECKPOINT_DB_USER=<имя_пользователя_базы_данных>
CHECKPOINT_DB_PASSWORD=<пароль_пользователя>

DJANGO_SECRET_KEY=<секретный_ключ>

DJANGO_DEBUG=False
```

Переменная `DJANGO_DEBUG` должна иметь значение `False` на production-сервере.

## Как запустить сайт

В терминале перейдите в папку с проектом и введите команду:
```
python manage.py runserver
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).