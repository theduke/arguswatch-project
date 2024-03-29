"""
WSGI config for myargus project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/wsgi/
"""

import os
import sys

# Add apps and lib directories to the python path.
DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(DIR))

from myargus import settings
sys.path.append(os.path.join(settings.BASE_DIR, 'lib'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myargus.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
