"""Development settings and globals."""

from .base import *

# -------------------------------------
# DJANGO CONFIGURATION
# -------------------------------------

# Django Setup
# =====================================

DEBUG = True

ALLOWED_HOSTS += ("docker.local", ".ngrok.io",)

SECRET_KEY = env("SECRET_KEY", default="CHANGEME!!!")

# Installed Apps
# =====================================

INSTALLED_APPS += (
    "debug_toolbar",
    "storages",
)

# Middleware
# =====================================

MIDDLEWARE += (
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)

# Logging
# =====================================

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        },
        "ratelimit": {
            "()": "app.utils.error_ratelimit_filter.RateLimitFilter",
        }
    },
    "formatters": {
        "verbose": {
            "format": "%(name)s %(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {
            "format": "%(levelname)s %(asctime)s %(message)s"
        },
    },
    "handlers": {
        "stream": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "slack": {
            "level": "ERROR",
            "class": "app.utils.log.SlackHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "handlers": ["stream"],
            "level": "WARNING",
            "propagate": False,
        },
        "django.db": {
            "handlers": ["stream"],
            "level": "WARNING",
            "propagate": False,
        },
        "django": {
            "handlers": ["stream"],
            "level": "WARNING",
            "propagate": False,
        },
        "z.pool": {
            "handlers": ["stream"],
            "level": "WARNING",
            "propagate": False,
        },
    }
}

# -------------------------------------
# VENDOR CONFIGURATION
# -------------------------------------

# Django Debug Toolbar
# =====================================


def show_toolbar(request):
    return True


INTERNAL_IPS = ("127.0.0.1",)

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}
