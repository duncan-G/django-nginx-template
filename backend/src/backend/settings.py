"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 1.11.4.
"""
from __future__ import absolute_import
import environ
from celery.schedules import crontab
from datetime import timedelta

root = environ.Path(__file__) - 4
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env(env_file=root('.env'))


SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*', ]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'django_celery_beat',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    try:
        import debug_toolbar  # noqa: F401

        INSTALLED_APPS += [
            'debug_toolbar',
        ]

        MIDDLEWARE += [
            'debug_toolbar.middleware.DebugToolbarMiddleware',
        ]

        def custom_show_toolbar(self):
            return True

        DEBUG_TOOLBAR_CONFIG = {
            'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
        }

    except ImportError:
        pass
    
ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': env.db(),
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DEFAULT_FILE_STORAGE = env('DEFAULT_FILE_STORAGE', default='django.core.files.storage.FileSystemStorage')

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = env('STATIC_URL', default='/static/')

STATIC_ROOT = env('STATIC_ROOT', default=root('static'))

MEDIA_URL = env('MEDIA_URL', default='/media/')

MEDIA_ROOT = env('MEDIA_ROOT', default=root('media'))

EMAIL_CONFIG = env.email_url(
    'EMAIL_URL', default='consolemail://')

vars().update(EMAIL_CONFIG)

#Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE':100,
}
    
# AWS
AWS_REGION = env('AWS_REGION', default='us-east-1')

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', default='')

AWS_ACCESS_SQS_KEY_ID = env('AWS_ACCESS_SQS_KEY_ID',default='')

AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', default='')

AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME', default='')

AWS_SECRET_ACCESS_SQS_KEY = env('AWS_SECRET_ACCESS_SQS_KEY',default='')

AWS_S3_REGION_NAME = AWS_REGION

#Celery
CELERY_BROKER_TRANSPORT = 'sqs'
CELERY_BROKER_TRANSPORT_OPTIONS = {
    'region': 'us-east-1',
    'queue_name_prefix': 'backend-'
}
CELERY_BROKER_USER = AWS_ACCESS_SQS_KEY_ID
CELERY_BROKER_PASSWORD = AWS_SECRET_ACCESS_SQS_KEY
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_SEND_EVENTS = True
CELERY_TASK_DEFAULT_QUEUE = 'celery'
"""
#Route different tasks to different queues
#Useful for APIs. Create a queue for each API integration
CELERY_TASK_ROUTES = {
    'task': {
        'queue': 'queue_name',
    },
}
"""
  
CELERY_BEAT_SCHEDULE = {
    'test_queue': {
        'task': 'core.tasks.test_queue',
        'schedule': timedelta(seconds=30),
    },
}
    

