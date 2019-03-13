"""
Django settings for chivote project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from decouple import config
from celery.schedules import crontab

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY_DEV_ONLY = 'abj*h0p8*n1az4sfa%kxp0s4&88^k$k&gw8vi)-ig!i@cq@=p&'
SECRET_KEY = config('DJANGO_SECRET_KEY', default=SECRET_KEY_DEV_ONLY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = []
ALLOWED_HOSTS += ['127.0.0.1', 'localhost']
ALLOWED_HOSTS += ['testserver']
ALLOWED_HOSTS += [config('DJANGO_URL_ENDPOINT', default=''), ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'livereload',
    'django.contrib.staticfiles',
    'apps.core',
    'apps.candidates',
    'apps.places',
    'apps.offices',
    'apps.newsfeed',
    'apps.races',
    # 'apps.questionnaires',
    'apps.site_content',
    'adminsortable2',
    'apps.scrape'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chivote.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'chivote.context_processors.app_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'chivote.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('PG_NAME'),
        'USER': config('PG_USER'),
        'PASSWORD': config('PG_PASSWORD', default=''),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', 'English'),
    ('es', 'Spanish'),
)

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'chivote/locale/')
]

CHIVOTE_URL_PREFIX = config('CHIVOTE_URL_PREFIX', default='')
CHIVOTE_IS_RUNOFF = config('CHIVOTE_IS_RUNOFF', default=False, cast=bool)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# suppress S3BotoS3Storage warning
AWS_DEFAULT_ACL = None

# django-bakery settings
INSTALLED_APPS += ('bakery',)
BUILD_DIR = os.path.join(BASE_DIR, 'build')
BAKERY_VIEWS = (
    'apps.core.views.HomePageView',
    'chivote.views.IndexView',
    'apps.races.views.RaceDetailView',
    'apps.races.views.RaceListView',
    'apps.races.views.ResultsListView',
    'apps.site_content.views.ContentItemDetailView',
    'apps.core.views.ErrorView',
    'apps.races.feeds.RaceFeed',
    'apps.newsfeed.feeds.LatestArticlesFeed'
)

AWS_BUCKET_NAME = config('AWS_BUCKET_NAME')
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_REGION = config('AWS_REGION')
BAKERY_GZIP = config('BAKERY_GZIP', default=False, cast=bool)
ALLOW_BAKERY_AUTO_PUBLISHING = config(
    'ALLOW_BAKERY_AUTO_PUBLISHING', default=False, cast=bool)

# webpack_loader settings
INSTALLED_APPS += ('webpack_loader', )

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend/bundles/webpack-stats.json')
    },
    'SSR': {
        'BUNDLE_DIR_NAME': 'server/',
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend/bundles/webpack-stats-server.json')
    }
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'frontend/bundles/prod'),
    os.path.join(BASE_DIR, 'precinct_lookup')
)

# ckeditor settings
INSTALLED_APPS += ('ckeditor', )

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    },
    'full': {
        'toolbar': 'full',
        'allowedContent': True
    }
}

# br settings
BALLOT_READY_API_KEY = config('BALLOT_READY_API_KEY')
BALLOT_READY_API_URL = config('BALLOT_READY_API_URL')

# ri settings
IL_SUNSHINE_API_URL = config('IL_SUNSHINE_API_URL')

# colorfield settings
INSTALLED_APPS += ('colorfield', )

# celery settings
# Celery application definition
# http://docs.celeryproject.org/en/v4.0.2/userguide/configuration.html

if config('CELERY_BROKER_URL', default=None):
    CELERY_BROKER_URL = config('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_TIMEZONE = TIME_ZONE

    CELERY_BEAT_SCHEDULE = {
        # 'update_br_candidates_all': {
        #     'task': 'apps.candidates.tasks.update_br_candidates_all',
        #     'schedule': crontab(day_of_week='mon-fri', hour='8-18/2')
        #     # Monday through Friday, every 2 hours 8am to 6pm
        # }
        'update_ri_candidates_all': {
            'task': 'apps.candidates.tasks.update_ri_candidates_all',
            'schedule': crontab(day_of_week='mon-fri', hour='7', minute='0')
        },
    }
