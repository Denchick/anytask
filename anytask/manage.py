#!/usr/bin/env python
import locale
import os
import sys

locale.setlocale(locale.LC_ALL, '')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
