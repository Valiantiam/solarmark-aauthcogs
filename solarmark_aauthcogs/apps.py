"""
Application config
"""

# Django
from django.apps import AppConfig

from . import __version__


class SolarmarkAAuthCogConfig(AppConfig):
    name = "solarmark_aauthcogs"
    label = "solarmark_aauthcogs"
