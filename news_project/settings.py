

import os
from pathlib import Path
from pickle import TRUE

from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news_app',
    'accounts',
    'hitcount',
    'modeltranslation',
    'whitenoise.runserver_nostatic',
  
    

]
MODELTRANSLATION_DEFAULT_LANGUAGE='uz'
USE_I18N = True
LOCALE_PATHS=BASE_DIR,'locale'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'news_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'news_app.context_processor.latest_news'
            ],
        },
    },
]

WSGI_APPLICATION = 'news_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/
from django.utils.translation import gettext_lazy as _




LANGUAGE_CODE = 'uz-uz'
LANGUAGES=[
    ('uz',_('Uzbek')),
    ('en',_("English")),
    ('ru',_("Russian")),
]

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS=[BASE_DIR/'static']
# STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]

MEDIA_URL='media/'
NEDIA_ROOT=BASE_DIR/'media/'
STATIC_ROOT=BASE_DIR/'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR/'static']
# STATIC_ROOT = '/home/host3649/newsnow.uz/django/staticfiles'
# STATICFILES_DIRS = ('/home/host3649/newsnow.uz/django/static', )
STATICFILES_FINDERS=[
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEDIA_URL='media/'
NEDIA_ROOT=BASE_DIR/'media/'
# MEDIA_ROOT='/home/host3649/newsnow.uz/django/media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL='home_page'
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
LOGIN_URL='login'
STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'
