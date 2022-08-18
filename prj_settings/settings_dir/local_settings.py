# Local environment-specific settings
from .base_settings import *

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t06(@md(eubjirw-@+romsc3#82f(uhf0pl7f(l-%3=1i#5w7+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# hosts
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "ADaaS.com"]

WSGI_APPLICATION = 'prj_settings.wsgi_local.application'
