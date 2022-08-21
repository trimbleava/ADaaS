"""
Environmentally independent settings 
For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/

"""

import os, sys
from pathlib import Path
from django.conf.global_settings import STATICFILES_FINDERS


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
 
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'gui',
    'reviews'
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

#...other environmentally independent settings 
# (TEMPLATES, WSGI_APPLICATION, TIME_ZONE, STATIC_ROOT etc.)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

#
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# As a brief recap:
# STATIC_URL is the URL location of static files located in STATIC_ROOT
# STATICFILES_DIRS tells Django where to look for static files in a Django project, such as a top-level static folder
# STATIC_ROOT is the folder location of static files when collectstatic is run
# STATICFILES_STORAGE is the file storage engine used when collecting static files with the collectstatic command.
#
STATIC_URL = "/static/"  
STATIC_ROOT = BASE_DIR / "staticfiles" 
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

MEDIA_ROOT = ""
MEDIA_URL = 'media/'

# ================ may need separation per environment later on ===========================

ROOT_URLCONF = 'prj_settings.urls'  

# Create new JWT key in REST_FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
# =========================================================================================

#
# mail default settting
#

DEFAULT_FROM_EMAIL = 'beheenMT@gmail.com'                           # Default: 'webmaster@localhost'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # send email to console
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'dndihprbfddqbivw'                            # app id for ADaaS, registered on beheenMT account
EMAIL_HOST_USER = 'beheenMT@gmail.com'
EMAIL_PORT = 465
EMAIL_USE_LOCALTIME = True
EMAIL_USE_SSL = True             # port=465
EMAIL_USE_TLS = False            # port=587
EMAIL_SSL_CERTFILE = None        # if true, path to a PEM-formatted certificate chain file 
EMAIL_SSL_KEYFILE = None         # if true, path to a PEM-formatted private key file
EMAIL_TIMEOUT = None

#
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-fieldSSS

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
