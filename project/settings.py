import os

import dj_database_url
from environs import Env


env = Env()
env.read_env()

DATABASES = {
    'default': dj_database_url.parse(
        env('CHECKPOINT_DATABASE_URL'),
    )
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('DJANGO_SECRET_KEY')

DEBUG = env.bool('DJANGO_DEBUG')

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
