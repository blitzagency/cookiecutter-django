from django.apps import AppConfig


class Config(AppConfig):
    name = "app.ui_kit"
    label = "app_ui_kit"
    verbose_name = "UI Kit"

    def ready(self):
        pass
