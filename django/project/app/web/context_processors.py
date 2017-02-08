def web_settings(request):
    from django.conf import settings

    return {
        "web_settings": {
            # "foo": getattr(settings, FOO, None)
        }
    }
