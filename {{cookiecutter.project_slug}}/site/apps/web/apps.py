from django.apps import AppConfig

import logging

log = logging.getLogger(__name__)


class Config(AppConfig):
    name = "app.web"
    label = "app_web"
    verbose_name = "Web App"

    def ready(self):
        pass
