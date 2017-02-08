from django.apps import AppConfig

import logging

log = logging.getLogger(__name__)


class Config(AppConfig):
    name = "app.utils"
    label = "app_utils"
    verbose_name = "Utils"

    def ready(self):
        pass
