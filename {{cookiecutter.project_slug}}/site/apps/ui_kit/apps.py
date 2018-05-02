from django.apps import AppConfig


class Config(AppConfig):
    name = 'apps.ui_kit'
    label = 'ui_kit'
    verbose_name = 'UI Kit'

    def ready(self):
        pass
