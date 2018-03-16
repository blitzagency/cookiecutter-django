'''Development settings and globals.'''

from .base import *  # noqa F402

# -------------------------------------
# DJANGO CONFIGURATION
# -------------------------------------

# Django Setup
# =====================================

ALLOWED_HOSTS += ('docker.local', '.ngrok.io',)  # noqa F405
SECRET_KEY = env('SECRET_KEY', default='abcdefghijklmnopqrstuvwxyz')  # noqa F405

INSTALLED_APPS += (  # noqa F405
    'debug_toolbar',
    'storages',
)

MIDDLEWARE += (  # noqa F405
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(name)s %(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'stream': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },

    'loggers': {
        '': {
            'handlers': ['stream', ],
            'level': LOG_LEVEL,  # noqa F405
            # 'propagate': False,
        },
        'django.db': {
            'handlers': ['stream', ],
            'level': LOG_LEVEL,  # noqa F405
            # 'propagate': False,
        },
        'z.pool': {
            'handlers': ['stream', ],
            'level': LOG_LEVEL,  # noqa F405
            # 'propagate': False,
        },
        'django': {
            'handlers': ['stream', ],
            'level': LOG_LEVEL,  # noqa F405
            # 'propagate': False,
        },
    }
}

INTERNAL_IPS = ('127.0.0.1',)


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}


# -------------------------------------
# VENDOR CONFIGURATION
# -------------------------------------
