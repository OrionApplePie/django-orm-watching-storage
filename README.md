# Веб-приложение пульт охраны хранилища банка

Приложения для учета посещений сотрудниками хранилища банка.
В базе данных ведется учет пропусков и фиксируются все посещения. Приложение позволяет охраннику отслеживать всех кто находится внутри хранилища, а также выявлять подозрительные посещения.

## Требования

Должно быть установлены следующее ПО:

- [Python 3.x](https://www.python.org/)
- [Git](https://git-scm.com/download)

Дополнительно для Windows можно использовать:

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

Создайте файл `.env` в корне проекта. Внесите следующие данные:
```
CHECKPOINT_DATABASE_URL=<postgres://USER:PASSWORD@HOST:PORT/NAME>

DJANGO_SECRET_KEY=<секретный_ключ>
DJANGO_ALLOWED_HOSTS=<ваш_домен1,ваш_домен2>
DJANGO_DEBUG=False
```
В переменную `CHECKPOINT_DATABASE_URL` вносится строка для подключения к БД.
Здесь приведен пример схемы строки подключения для Postgresql, схемы для других СУБД по [ссылке](https://github.com/jacobian/dj-database-url#url-schema).

В переменную `DJANGO_ALLOWED_HOSTS` нужно внести список хостов/доменов, для которых может работать текущий сайт. Если таковых несколько, то внесите их через запятую. Это необходимо для [безопасности](https://djbook.ru/rel1.7/ref/settings.html#allowed-hosts).

Переменная `DJANGO_DEBUG` должна иметь значение `False` на production-сервере.

## Как запустить сайт

В терминале перейдите в папку с проектом и введите команду:
```
python manage.py runserver
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).