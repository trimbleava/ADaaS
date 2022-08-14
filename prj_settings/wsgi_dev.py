import os

from django.core.wsgi import get_wsgi_application

from prj_settings.wsgi import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prj_settings.settings_dir.dev_settings')

application = get_wsgi_application()
