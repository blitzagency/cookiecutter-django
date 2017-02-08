from django.apps import AppConfig


class Config(AppConfig):
    name = "app.ui"
    label = "app_ui"
    verbose_name = "UI Kit"

    def ready(self):
        pass
