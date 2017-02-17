"""
Common settings and globals.

See:
    - https://docs.djangoproject.com/en/dev/topics/settings/
    - https://docs.djangoproject.com/en/dev/ref/settings/
"""
import environ
from os.path import abspath, basename, dirname, join, normpath

# -------------------------------------
# GENERAL SETUP
# -------------------------------------

# Paths
# =====================================
# Paths here the `environ.Path` which provides a special api around os paths.
#
# How to use:
#
#   # Get the path as a string
#   PROJECT_PATH()
#
#   # Get a sub-directory or file path as a string
#   # Note: This calls the path directly and not through .path
#   PROJECT_PATH("static")
#   PROJECT_PATH("foo.json")
#
#   # Get a path as an environ Path object
#   PROJECT_PATH.path("static")
#
# Docs:
#   - https://github.com/joke2k/django-environ

WORKING_PATH = environ.Path(__file__) - 1

DJANGO_PATH = WORKING_PATH - 4

PROJECT_PATH = DJANGO_PATH.path("project")

APP_PATH = PROJECT_PATH.path("app")

# Env
# =====================================

env = environ.Env()
environ.Env.read_env(DJANGO_PATH(".env"))

# -------------------------------------
# DJANGO CONFIGURATION
# -------------------------------------

# Django Setup
# =====================================

WSGI_APPLICATION = "app.config.wsgi.application"

ROOT_URLCONF = "app.config.urls"

DEBUG = env.bool("DEBUG", False)

ALLOWED_HOSTS = ("localhost", "127.0.0.1",)

SITE_ID = 1

SITE_NAME = "example.com"

ADMINS = (
    ("app admin"),
)

MANAGERS = ADMINS

FIXTURE_DIRS = (
    PROJECT_PATH("fixtures"),
)

# Installed Apps
# =====================================

INSTALLED_APPS = (
    # Overrides
    # Apps that must come first (may include local apps)
    "app.utils",
    "grappelli_safe",
    "filebrowser_safe",

    # Django apps
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.redirects",
    "django.contrib.admin",

    # Local apps
    "app.web",
    "app.ui_kit",

    # Third-party Apps
    "django_extensions",
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.pages",
    "mezzanine.forms",
    "mezzanine.galleries",
    "redactor",
    "adminsortable2",
)

# Middleware
# =====================================

MIDDLEWARE = (
    # Default Django middleware.
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # Mezzanine
    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.RedirectFallbackMiddleware",
    "mezzanine.core.middleware.TemplateForDeviceMiddleware",
    "mezzanine.core.middleware.TemplateForHostMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "mezzanine.core.middleware.SitePermissionMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
)

# Databases
# =====================================

DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    "default": env.db("DATABASE_URL",
                      default="postgres://vagrant:vagrant@postgres/vagrant"),
}

# Templates
# =====================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": (
            APP_PATH("overrides/templates"),
        ),
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": (
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
                "app.utils.context_processors.global_variables",
                "app.web.context_processors.web_settings",
                "mezzanine.conf.context_processors.settings",
                "mezzanine.pages.context_processors.page",
            ),
            "builtins": [
                "mezzanine.template.loader_tags",
            ],
        },
    }
]

# Staticfiles
# =====================================

STATIC_ROOT = PROJECT_PATH("collected-static")

STATIC_URL = "/static/"

# Add project/static to staticfile resolution
# Entries here are eligible for `collectstatic` as well
# See:
# https://docs.djangoproject.com/en/1.10/ref/contrib/staticfiles/#collectstatic
STATICFILES_DIRS = (
    PROJECT_PATH("static"),
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

SERVE_STATIC = False

MEDIA_ROOT = PROJECT_PATH("media")

MEDIA_URL = "/media/"

# Locale / I18N & L10N
# =====================================

# Set to True to automatically enable django's i81n
# Note: This is a custom (i.e., non-native Django setting) but is used to
#       branch in a few places to enable Django's I18N and L10N automatically.
AUTO_ENABLE_I18N = {% if cookiecutter.use_i18n.lower() == "y" %}True{% else %}False{% endif %}

TIME_ZONE = "America/Los_Angeles"

USE_TZ = True

USE_I18N = AUTO_ENABLE_I18N
USE_L10N = AUTO_ENABLE_I18N

LANGUAGE_CODE = "en"

LANGUAGES = (
    ("en", "English"),
    # Add additional / change languages here
    # ("de", "German")
)

# Authentication
# =====================================

AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)

ACCOUNT_AUTHENTICATION_METHOD = "username"

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = "mandatory"

ACCOUNT_ALLOW_REGISTRATION = env.bool(
    "ACCOUNT_ALLOW_REGISTRATION", False)

# Cache
# =====================================

CACHE_TIMEOUT = env("CACHE_TIMEOUT", default=60 * 60)

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "TIMEOUT": CACHE_TIMEOUT,
    }
}

# -------------------------------------
# THIRD-PARTY CONFIGURATION
# -------------------------------------

# Grapelli
# =====================================

GRAPPELLI_ADMIN_TITLE = "{{cookiecutter.project_name}}"

# Celery
# =====================================

CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

# Redis
# =====================================

REDIS_HOST = env("REDIS_HOST", default="redis://localhost:6379")

# Storages
# =====================================

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", default="")

AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", default="")

AWS_BUCKET_NAME = AWS_STORAGE_BUCKET_NAME = env("AWS_BUCKET_NAME", default="")

AWS_QUERYSTRING_AUTH = False

USE_HTTPS_FOR_ASSETS = env.bool("USE_HTTP_FOR_ASSETS", False)

AWS_IS_GZIPPED = True

ASSET_VERSION = env("ASSET_VERSION", default=False)

# Mezzanine
# =====================================

USE_MODELTRANSLATION = False

PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"

PACKAGE_NAME_GRAPPELLI = "grappelli_safe"

INLINE_EDITING_ENABLED = True

SITE_TITLE = GRAPPELLI_ADMIN_TITLE

RICHTEXT_WIDGET_CLASS = "redactor.widgets.RedactorEditor"

{% if cookiecutter.use_uploadcare.lower() == "y" %}
# UploadCare
# =====================================

UPLOADCARE = {
    "pub_key": env("UPLOADCARE_PUB_KEY", default=""),
    "secret": env("UPLOADCARE_SECRET_KEY", default=""),
}
{% endif %}

# Redactor
# =====================================

REDACTOR_OPTIONS = {
    "lang": "en",
    {% if cookiecutter.use_uploadcare.lower() == "y" %}
    "plugins": ["uploadcare"],
    "uploadcare": {
        "publicKey": UPLOADCARE["pub_key"],
        "crop": "free",
        "tabs": "all",
    }
    {% endif %}
}

REDACTOR_UPLOAD = "uploads/"

# -------------------------------------
# DYNAMIC SETTINGS
# -------------------------------------

# Calling set_dynamic_settings() will rewrite globals
# based on what has been defined so far,
# in order to provide some better defaults.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())
