from __future__ import print_function

import logging
import os

from django.core.management.base import BaseCommand
from django.conf import settings

logger = logging.getLogger('gui')


from gui.models import Tools

# system default data directory
if 'DATA_SHARE' not in os.environ:
    os.environ['DATA_SHARE'] = settings.DATA_DIR

# to run for tenant: python manage.py tenant_command load_drive -s schema
# to run for public: python manage.py load_tools
class Command(BaseCommand):

    def handle(self, *args, **options):

        root = Tools.objects.create(name="Tools")
        nwm = Tools.objects.create(name="NWM Coastal", parent=root)
        Tools.objects.create(name="Grid 250m", parent=nwm)
        Tools.objects.create(name="Grid 1km", parent=nwm)

        dflow = Tools.objects.create(name="DFlow FM", parent=root)
        Tools.objects.create(name="Grid Unstructured", parent=dflow)