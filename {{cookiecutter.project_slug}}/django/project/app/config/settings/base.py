"""
Common settings and globals.

See:
    - https://docs.djangoproject.com/en/dev/topics/settings/
    - https://docs.djangoproject.com/en/dev/ref/settings/
"""
import re
import environ
from os.path import join

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

SITE_NAME = env("SITE_NAME", default="example.com")

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
    "djangocms_admin_style",
    "app.utils",

    # Django apps
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.redirects",
    "django.contrib.admin",
    # "django.contrib.gis",
    # "django.contrib.gis.geoip",

    # DjangoCMS Apps
    "cms",
    "menus",
    "sekizai",
    "treebeard",
    "djangocms_text_ckeditor",
    "filer",
    "easy_thumbnails",
    "djangocms_link",
    "cmsplugin_filer_file",
    "cmsplugin_filer_folder",
    "cmsplugin_filer_image",
    "cmsplugin_filer_utils",
    "djangocms_style",
    "djangocms_snippet",
    "djangocms_googlemap",
    "djangocms_video",
    "meta",

    # Local apps
    "app.web",
    "app.ui_kit",

    # Third-party Apps
    "django_extensions",
    "crispy_forms",
    "rest_framework",
    "rest_framework.authtoken",
    {% if cookiecutter.use_uploadcare.lower() == "y" %}
    "pyuploadcare.dj",
    {% endif %}
)

# Middleware
# =====================================

MIDDLEWARE = (
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # Must come first
    "cms.middleware.utils.ApphookReloadMiddleware",

    # Default Django middleware.
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",

    # DjangoCMS
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",
)

# Databases
# =====================================

DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    "default": env.db(
        "DATABASE_URL",
        default="postgres://djangodb:djangodb@postgres/djangodb"),
}

# DATABASES["default"]["ENGINE"] = "django.contrib.gis.db.backends.postgis"

# Logging
# =====================================

LOG_LEVEL = env("LOG_LEVEL", default="ERROR")

# Templates
# =====================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": (
            APP_PATH("overrides/templates"), "templates",
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

                # DjangoCMS
                "sekizai.context_processors.sekizai",
                "cms.context_processors.cms_settings",

                # Local
                "app.utils.context_processors.global_variables",
                "app.web.context_processors.web_settings",
            ),
        },
    }
]

# Storages
# =====================================

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", default="")

AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", default="")

AWS_BUCKET_NAME = AWS_STORAGE_BUCKET_NAME = env("AWS_BUCKET_NAME", default="")

AWS_QUERYSTRING_AUTH = False

USE_HTTPS_FOR_ASSETS = env.bool("USE_HTTPS_FOR_ASSETS", False)

AWS_IS_GZIPPED = True

ASSET_VERSION = env("ASSET_VERSION", default=False)

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

MEDIA_ROOT = PROJECT_PATH("uploads")

MEDIA_URL = "/uploads/"

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

LOCALE_PATHS = (
    PROJECT_PATH("app/web/locale"),
)

# Authentication
# =====================================

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

# GEO IP
# =====================================

# GEOIP_PATH = join(PROJECT_PATH(), "data", "GeoLite2-City.mmdb")

# -------------------------------------
# VENDOR CONFIGURATION
# -------------------------------------


# Celery
# =====================================

CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

# Redis
# =====================================

REDIS_HOST = env("REDIS_HOST", default="redis://localhost:6379")


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


# Thumbnails
# =====================================

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters"
)


# DjangoCMS
# =====================================
# See: https://docs.django-cms.org/en/release-3.4.x/

CMS_LANGUAGES = {
    "default": {
        "fallbacks": ["en", "es", "fr"],
        "redirect_on_fallback": True,
        "public": True,
        "hide_untranslated": False,
    }
}

CMS_TEMPLATES = (
    # Customize this
    ('web/fullwidth.html', 'Fullwidth'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}


# DjangoCMS Meta
# =====================================
# See: https://django-meta.readthedocs.io/en/latest/index.html

META_SITE_PROTOCOL = env("META_SITE_PROTOCOL", default="http")

META_USE_SITES = True

META_USE_OG_PROPERTIES = True

META_USE_TWITTER_PROPERTIES = True

META_USE_GOOGLEPLUS_PROPERTIES = True

META_DEFAULT_TYPE = "Article"

META_FB_TYPE = "Article"

META_FB_APPID = ""

META_FB_PROFILE_ID = "{{cookiecutter.project_slug}}"

META_FB_PUBLISHER = "https://www.facebook.com/{{cookiecutter.project_slug}}/"

META_TWITTER_TYPE = "summary"

META_TWITTER_SITE = "https://twitter.com/{{cookiecutter.project_slug}}"

META_GPLUS_TYPE = "Blog"

# Taggit / Taggit Autosuggest
# =====================================


def trim_trailing_slash(s):
    return re.sub("/$", "", s)


TAGGIT_AUTOSUGGEST_CSS_FILENAME = "taggit-autosuggest.css"

TAGGIT_AUTOSUGGEST_STATIC_BASE_URL = trim_trailing_slash(STATIC_URL)


# Slack
# =====================================

# SLACK_INCOMING_WEB_HOOK = env(
#     "SLACK_INCOMING_WEB_HOOK",
#     default="https://hooks.slack.com/services/xxxxx/xxxxx/"
#     "xxxxx")

# SLACK_CHANNEL = env(
#     "SLACK_CHANNEL", default="{{cookiecutter.project_slug}}-logs")

# SLACK_USER_NAME = env("SLACK_USER_NAME", default="Logger:DEV")


# Crispy Forms
# =====================================

CRISPY_TEMPLATE_PACK = "bootstrap3"

# Rest Framework
# =====================================

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    )
}

# -------------------------------------
# PROJECT SETTINGS
# -------------------------------------


# Analytics
# =====================================

GTM_CODE = env("GTM_CODE", default="")

OPTIMIZELY_ID = env("OPTIMIZELY_ID", default="")

# Misc
# =====================================

GOOGLE_API_KEY = env("GOOGLE_API_KEY", default="")
LIVECHAT_LICENSE = env("LIVECHAT_LICENSE", default="")
