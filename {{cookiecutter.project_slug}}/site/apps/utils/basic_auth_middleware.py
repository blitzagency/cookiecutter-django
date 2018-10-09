import base64
from django.http import HttpResponse
from django.middleware.common import CommonMiddleware
from django.conf import settings


_SETTINGS = getattr(settings, 'BASIC_AUTH', {})
USERNAME = _SETTINGS.get('USERNAME', None)
PASSWORD = _SETTINGS.get('PASSWORD', None)
USE_BASIC_AUTH = True if USERNAME and PASSWORD else False


class AuthMiddleware(CommonMiddleware):
    """
    Add this to middleware:
    'utils.basic_auth_middleware.AuthMiddleware',

    Add this to settings:
    BASIC_AUTH = {'USERNAME': 'user', 'PASSWORD': 'password'}
    """  # noqa

    def process_request(self, request):
        if USE_BASIC_AUTH:
            if request.META.get('HTTP_AUTHORIZATION', False):
                authtype, auth = request.META['HTTP_AUTHORIZATION'].split(' ')
                auth = base64.b64decode(auth).decode('utf-8')
                username, password = auth.split(':')
                if username == USERNAME and password == PASSWORD:
                    return
            response = HttpResponse('Auth Required', status=401)
            response['WWW-Authenticate'] = 'Basic realm="bat"'
            return response
