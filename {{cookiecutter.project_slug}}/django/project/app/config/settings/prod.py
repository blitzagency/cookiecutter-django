"""Production settings and globals."""

from .base import *

# -------------------------------------
# DJANGO CONFIGURATION
# -------------------------------------

# Django Setup
# =====================================

ALLOWED_HOSTS += (".herokuapp.com",)

SECRET_KEY = env("SECRET_KEY")

# Installed Apps
# =====================================

INSTALLED_APPS += (
    "gunicorn",
    "storages",
)

# Databases
# =====================================

DATABASES["default"]["ENGINE"] = "django_postgrespool"

DATABASE_POOL_ARGS = {
    "max_overflow": 7,
    "pool_size": 7,
    "recycle": 300,
}

# Staticfiles
# =====================================

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# DEFAULT_FILE_STORAGE = "app.utils.storage.MediaRootS3BotoStorage"

# ASSET_PROTOCOL = "https" if USE_HTTPS_FOR_ASSETS else "http"

# # THIS IS VERY IMPORTANT TO MAKE COMPRESSOR WORK!!!!!!
# ASSET_PORT = ":443" if USE_HTTPS_FOR_ASSETS else ""

# STATIC_URL = "{}://{}.s3.amazonaws.com{}/".format(
#     ASSET_PROTOCOL, AWS_STORAGE_BUCKET_NAME, ASSET_PORT)

# MEDIA_URL = "{}://{}.s3.amazonaws.com/uploads/".format(
#     ASSET_PROTOCOL, AWS_STORAGE_BUCKET_NAME)

# if ASSET_VERSION:
#     # set path of assets in s3 bucket, note this is '' by default
#     AWS_LOCATION = "%s/" % ASSET_VERSION
#     STATIC_URL += AWS_LOCATION

# Email / SMTP
# =====================================

# TODO: Update to use env

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = env("EMAIL_HOST", default="smtp.gmail.com")

EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")

EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="your_email@example.com")

EMAIL_PORT = env("EMAIL_PORT", default=587)

EMAIL_SUBJECT_PREFIX = "[%s] " % SITE_NAME

EMAIL_USE_TLS = True

SERVER_EMAIL = EMAIL_HOST_USER

# Logging
# =====================================

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
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
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false", "ratelimit"],
            "class": "django.utils.log.AdminEmailHandler"
        },
        "stream": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "slack": {
            "level": "ERROR",
            "class": "app.utils.log.SlackHandler",
            "formatter": "verbose",
        },
    },

    "loggers": {
        "": {
            "handlers": ["slack", "stream", ],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "django.db": {
            "handlers": ["slack", "stream", ],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "z.pool": {
            "handlers": ["slack", "stream", ],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "django": {
            "handlers": ["slack", "stream", ],
            "propagate": False,
        },
    }
}

# -------------------------------------
# VENDOR CONFIGURATION
# -------------------------------------

# Utils
# =====================================

SLACK_USER_NAME = env("SLACK_USER_NAME", default="Logger:PROD")

# Storages
# =====================================

AWS_HEADERS = {
    "Cache-Control": "max-age=31536000",
}
