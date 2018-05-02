from django.apps import AppConfig

import logging

log = logging.getLogger(__name__)


class Config(AppConfig):
    name = 'apps.web'
    label = 'web'
    verbose_name = 'Web App'

    def ready(self):
        pass
