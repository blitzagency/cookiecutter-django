from django.apps import AppConfig

import logging

log = logging.getLogger(__name__)


class Config(AppConfig):
    name = 'apps.utils'
    label = 'utils'
    verbose_name = 'Utils'

    def ready(self):
        pass
