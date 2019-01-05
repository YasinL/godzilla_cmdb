from django.test import TestCase

# # Create your tests here.
#
from  godzilla.handle.permission import check_permiss
import os
# import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","godzilla_cmdb.settings")
# django.setup()





if __name__ == '__main__':
    print('admin')
    print(os.environ.get('DJANGO_SETTINGS_MODULE'))





