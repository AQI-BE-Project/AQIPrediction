"""
WSGI config for aqiprediction project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
print("Current Working Directory: ", os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aqiprediction.settings')

application = get_wsgi_application()
