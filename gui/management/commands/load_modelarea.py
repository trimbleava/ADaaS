from __future__ import print_function

import logging

from django.core.management.base import BaseCommand

logger = logging.getLogger('rsmgui')

from rsmgui.models import ModelArea
from gisapp.models import SFBasin

# to run for public: python manage.py load_modelarea
# to run: python manage.py tenant_command load_modelarea -s schema
class Command(BaseCommand):

    def load_modelarea(self):
        msg = "Loading data for Model Area"
        #logger.info(msg)

        model_areas = SFBasin.objects.all()
        areas=[]
        for model in model_areas:
            areas.append(model)

        ModelArea.objects.bulk_create(areas)


    def handle(self, *args, **options):
        self.load_modelarea()
