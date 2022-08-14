from __future__ import print_function

import logging, sys
from django.core.management.base import BaseCommand


from gui.models import Layers

logger = logging.getLogger('gui')

# ./manage.py ogrinspect data/województwa.shp Voivodeship --mapping --srid 2180 --multi >> voivodeships/models.py
# to run for public: python manage.py load_layers
# to run: python manage.py tenant_command load_layers -s schema
class Command(BaseCommand):

    def load_layers(self):
        msg = "Loading data for gui layers"
        logger.info(msg)

    def handle(self, *args, **options):
        self.load_layers()
