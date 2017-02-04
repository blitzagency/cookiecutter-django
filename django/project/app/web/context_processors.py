from .models import Settings


def site(request):
    return {
        "site_settings": Settings.objects.first()
    }
