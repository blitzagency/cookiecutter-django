"""Development settings and globals."""

from .base import *


# ######### DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True


# ######### TOOLBAR CONFIGURATION
# See:
# https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
    'debug_toolbar',
    # 'storages',
)

# See:
# https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)

# See:
# https://github.com/django-debug-toolbar/django-debug-toolbar#installation


def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

MIDDLEWARE += (
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)
# ######### END TOOLBAR CONFIGURATION

# ######### STORAGE SETTINGS

STATICFILES_STORAGE = 'require.storage.OptimizedStaticFilesStorage'

# ######### END STORAGE SETTINGS


# ######### LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
#

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'ratelimit': {
            '()': 'app.utils.error_ratelimit_filter.RateLimitFilter',
        }
    },
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
            'formatter': 'simple',
        },
    },
    'loggers': {
        '': {
            'handlers': ['stream'],
            'level': 'WARNING',
            'propagate': False,
        },
        'sportlogos': {
            'handlers': ['stream'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db': {
            'handlers': ['stream'],
            'level': 'WARNING',
            'propagate': False,
        },
        'django': {
            'handlers': ['stream'],
            'level': 'WARNING',
            'propagate': False,
        },
        'z.pool': {
            'handlers': ['stream'],
            'level': 'WARNING',
            'propagate': False,
        },
    }
}
# ######### END LOGGING CONFIGURATION
