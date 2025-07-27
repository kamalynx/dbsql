import re
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

PUBLIC_PATH = BASE_DIR / 'public'

if not PUBLIC_PATH.exists():
    PUBLIC_PATH.mkdir()

env = environ.Env(
    DEBUG=(bool, False),
    TELEGRAM_BOT_TOKEN=(str, None),
    TELEGRAM_CHAT_ID=(str, None),
)
env.read_env(BASE_DIR / '.env')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.tuple('ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'debug_toolbar',
    'articles.apps.ArticlesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

if not DEBUG:
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
else:
    AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

STATIC_ROOT = PUBLIC_PATH / 'static/'
MEDIA_ROOT = PUBLIC_PATH / 'media/'

STATICFILES_DIRS = [
    BASE_DIR / 'assets',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SITE_ID = 1

INTERNAL_IPS = [
    '127.0.0.1',
]


DJANGORESIZED_DEFAULT_SIZE = 960, 720
DJANGORESIZED_DEFAULT_QUALITY = 100
DJANGORESIZED_DEFAULT_KEEP_META = False
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'WEBP'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis:///run/redis/redis-server.sock',
    },
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

CSRF_USE_SESSIONS = True

DISALLOWED_USER_AGENTS = (
    re.compile(r'curl/[\d.]+', re.IGNORECASE),
    re.compile(r'go-http-client/[\d.]+', re.IGNORECASE),
    re.compile(r'python-requests/[\d.]+', re.IGNORECASE),
    re.compile(r'axios/[\d.]+', re.IGNORECASE),
    re.compile(r'Wget/[\d.]+', re.IGNORECASE),
    re.compile(r'CMS-Checker/[\d.]+', re.IGNORECASE),
    re.compile(r'WhatCMS/[\d.]+', re.IGNORECASE),
    re.compile(r'2ip bot/[\d.]+', re.IGNORECASE),
    re.compile(r'BackupLand/[\d.]+', re.IGNORECASE),
    re.compile(r'HeadlessChrome/[\d.]+', re.IGNORECASE),
    re.compile(r'zgrab/[\d.]+', re.IGNORECASE),
    re.compile(r'Keydrop.io/[\d.]+', re.IGNORECASE),
    re.compile(r'CensysInspect/[\d.]+', re.IGNORECASE),
    re.compile(r'nvdorz'),
    re.compile(r'aiohttp/[\d.]+', re.IGNORECASE),
    re.compile(r'python-httpx/[\d.]+', re.IGNORECASE),
    re.compile(r'SiteCheckerBotCrawler/[\d.]+', re.IGNORECASE),
)

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage',
    },
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

TELEGRAM_BOT_TOKEN = env('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = env('TELEGRAM_CHAT_ID')

PAGINATE_BY = 10
