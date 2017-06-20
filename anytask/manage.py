#!/usr/bin/env python

import locale
import settings
import sys
import imp

from django.core.management import execute_manager

locale.setlocale(locale.LC_ALL, '')

try:
    imp.find_module('settings')  # Assumed to be in the same directory.
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. "
                     "It appears you've customized things.\n"
                     "You'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)


# To skip test_site_profile_not_available from django.contrib.auth.tests.models.ProfileTestCase
# see https://code.djangoproject.com/ticket/17966
sys.modules['django.contrib.auth.tests'] = None

if __name__ == "__main__":
    execute_manager(settings)
