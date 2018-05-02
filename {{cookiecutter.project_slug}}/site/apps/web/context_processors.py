def web_settings(request):
    from django.conf import settings

    return {
        "web_settings": {
            "debug": getattr(settings, "DEBUG", False),
            "auto_enable_i18n": getattr(settings, "AUTO_ENABLE_I18N", False),
            "gtm_code": getattr(settings, "GTM_CODE", ""),
            "optimizely_id": getattr(settings, "OPTIMIZELY_ID", ""),
            "google_api_key": getattr(settings, "GOOGLE_API_KEY", ""),
            "livechat_license": getattr(settings, "LIVECHAT_LICENSE", ""),
        }
    }
