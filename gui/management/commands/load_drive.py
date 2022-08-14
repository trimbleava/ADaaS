from __future__ import print_function

import logging
import os

from django.core.management.base import BaseCommand
from django.conf import settings

logger = logging.getLogger('gui')
#logger.log("testing")

from gui.models import Drive

# system default data directory
if 'DATA_SHARE' not in os.environ:
    os.environ['DATA_SHARE'] = settings.DATA_DIR

# see the original codes in test
class FileTreeMaker(object):

    def _recurse(self, parent_path, parent,file_list, prefix, output_buf, level):
        if len(file_list) == 0 \
            or (self.max_level != -1 and self.max_level <= level):
            return
        else:
            # lambda arguments: expression
            # double = lambda x: x * 2  run: double(5)
            # new_list = list(filter(lambda x: (x%2 == 0) , my_list))
            # new_list = list(map(lambda x: x * 2 , my_list))
            # sort by attribute of an object:
            # To sort the list in place...
            # [<Tag: 128>, <Tag: 2008>, <Tag: <>, <Tag: actionscript>, <Tag: addresses>, <Tag: aes>, <Tag: ajax> ...]
            # ut[1].count  --> ut.sort(key=lambda x: x.count, reverse=True)
            # To return a new list, use the sorted() built-in function...
            # newlist = sorted(ut, key=lambda x: x.count, reverse=True)

            file_list.sort(key=lambda f: os.path.isfile(os.path.join(parent_path, f)), reverse=False)
            # ['docs', 'labs', 'lectures', 'rsm', 'testfolder', 'setup_rsm']

            for idx, sub_path in enumerate(file_list):
                if any(exclude_name in sub_path for exclude_name in self.exn):
                    continue

                full_path = os.path.join(parent_path, sub_path)
                idc = "|---"
                if idx == len(file_list) - 1:
                    idc = "|___"     # for closing end of tree

                if os.path.isdir(full_path) and sub_path not in self.exf:
                    output_buf.append("%s%s[%s] (%d)" % (prefix, idc, sub_path, level))
                    new_parent = Drive.objects.create(name=sub_path, parent=parent)

                    if len(file_list) > 1 and idx != len(file_list) - 1:
                        tmp_prefix = prefix + "|  "
                    else:
                        tmp_prefix = prefix + "    "

                    self._recurse(full_path, new_parent, os.listdir(full_path), tmp_prefix, output_buf, level + 1)

                elif os.path.isfile(full_path):
                    output_buf.append("%s%s%s (%d)" % (prefix, idc, sub_path, level))
                    Drive.objects.create(name=sub_path, parent=parent)


    def make(self):
        self.root = os.environ['DATA_SHARE']
        self.exf = []
        self.exn = ['gis']            # do not add gis directory and its contents
        self.max_level = -1

        print("root:%s" % self.root)


        buf = []
        path_parts = self.root.rsplit(os.path.sep, 1)
        buf.append(("[%s], %d") % (path_parts[-1],0))

        parent = Drive.objects.create(name=path_parts[1])
        self._recurse(self.root, parent, os.listdir(self.root), "", buf, 1)


# to run for tenant: python manage.py tenant_command load_drive -s schema
# to run for public: python manage.py load_drive
class Command(BaseCommand):

    def handle(self, *args, **options):
        FileTreeMaker().make()
