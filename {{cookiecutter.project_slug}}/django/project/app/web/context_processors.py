def web_settings(request):
    from django.conf import settings

    return {
        "web_settings": {
            "debug": getattr(settings, "DEBUG", False),
            "auto_enable_i18n": getattr(settings, "AUTO_ENABLE_I18N", False)
        }
    }
