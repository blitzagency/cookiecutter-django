from django.apps import AppConfig

import logging

log = logging.getLogger(__name__)


class AppWebConfig(AppConfig):
    name = "app.web"
    label = "app_web"
    verbose_name = "Application Name"

    def ready(self):
        pass
