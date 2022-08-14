# Production environment-specific settings

import os

'SECRET': os.environ.get('SECRET_KEY')

WSGI_APPLICATION = 'PRJ_SETTINGS.wsgi_prod.application'