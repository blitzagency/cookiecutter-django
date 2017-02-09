def web_settings(request):
    from django.conf import settings

    return {
        "web_settings": {
            "auto_enable_i18n": getattr(settings, "AUTO_ENABLE_I18N", False)
        }
    }
