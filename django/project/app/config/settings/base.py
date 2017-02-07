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

# TODO: Update paths below to use env paths, e.g, ROOT_DIR =
# environ.Path(__file__) - 3

DJANGO_ROOT = dirname(dirname(abspath(__file__)))

SITE_ROOT = dirname(DJANGO_ROOT)

PROJECT_ROOT = abspath(join(dirname(__file__), '../../../'))

# Env
# =====================================

# TODO: Path to env is clunky, see note in # Paths
env = environ.Env()
environ.Env.read_env(abspath(join(PROJECT_ROOT, "../.env")))

# -------------------------------------
# DJANGO CONFIGURATION
# -------------------------------------

# Django Setup
# =====================================

WSGI_APPLICATION = 'app.config.wsgi.application'

ROOT_URLCONF = 'app.config.urls'

DEBUG = env.bool("DEBUG", False)

ALLOWED_HOSTS = ("localhost", "127.0.0.1",)

SITE_ID = 1

# TODO: This resolves to "config", probably not correct.
SITE_NAME = basename(DJANGO_ROOT)

# NOTE: This key only used for development and testing!
SECRET_KEY = env(
    "SECRET_KEY", default=r"f2(!%hox^koxhw%%0a)@@!f5^7lu(1$@es*#1szh2q^@3der$")

ADMINS = (
    ('app admin'),
)

MANAGERS = ADMINS

# Testing
# =====================================

TEST_RUNNER = 'testing.PytestTestRunner'

# TODO: Update to use env paths
FIXTURE_DIRS = (
    normpath(join(PROJECT_ROOT, 'fixtures')),
)

# Installed Apps
# =====================================

INSTALLED_APPS = (
    # Apps that must come first (may include local apps)
    'app.utils.apps.AppUtilsConfig',
    'grappelli_safe',
    'filebrowser_safe',

    # Django Apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects',


    # Local apps
    # TODO: leverage __init__.default_app_config, `default_app_config =
    # "rock_n_roll.apps.RockNRollConfig"`
    'app.web.apps.AppWebConfig',


    # Third-party Apps
    'django_extensions',
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.pages",
    "mezzanine.forms",
    "mezzanine.galleries",
    'redactor',
    'adminsortable2',

)

# Middleware
# =====================================
# Middleware Ordering Info:
# https://docs.djangoproject.com/en/1.10/ref/middleware/#middleware-ordering

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

# TODO: Update to use env paths
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": (normpath(
            join(PROJECT_ROOT, "app", "overrides", "templates")),),
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

# TODO: Update to use env paths

STATIC_ROOT = join(PROJECT_ROOT, 'collected-static')

STATIC_URL = '/static/'

SERVE_STATIC = False

MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

MEDIA_URL = '/media/'

# Locale / I18N & L10N
# =====================================

TIME_ZONE = "America/Los_Angeles"

LANGUAGE_CODE = 'en-us'

USE_I18N = False

USE_L10N = False

USE_TZ = True

# Authentication
# =====================================

AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)

ACCOUNT_AUTHENTICATION_METHOD = "username"

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = "mandatory"

ACCOUNT_ALLOW_REGISTRATION = env.bool(
    "ACCOUNT_ALLOW_REGISTRATION", True)

# Cache
# =====================================

CACHE_TIMEOUT = env("CACHE_TIMEOUT", default=60 * 60)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': CACHE_TIMEOUT,
    }
}

# -------------------------------------
# THIRD-PARTY CONFIGURATION
# -------------------------------------

# Grapelli
# =====================================

GRAPPELLI_ADMIN_TITLE = "project_name"

# Celery
# =====================================

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Redis
# =====================================

REDIS_HOST = env("REDIS_HOST", default='redis://localhost:6379')

# Storages
# =====================================

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')

AWS_BUCKET_NAME = AWS_STORAGE_BUCKET_NAME = env("AWS_BUCKET_NAME")

AWS_QUERYSTRING_AUTH = False

USE_HTTPS_FOR_ASSETS = env.bool('USE_HTTP_FOR_ASSETS', False)

AWS_IS_GZIPPED = True

ASSET_VERSION = env("ASSET_VERSION", default=False)

# Mezzanine
# =====================================

USE_MODELTRANSLATION = False

PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"

PACKAGE_NAME_GRAPPELLI = "grappelli_safe"

INLINE_EDITING_ENABLED = True

SITE_TITLE = GRAPPELLI_ADMIN_TITLE

RICHTEXT_WIDGET_CLASS = 'redactor.widgets.RedactorEditor'

# UploadCare
# =====================================

UPLOADCARE = {
    'pub_key': env('UPLOADCARE_PUB_KEY'),
    'secret': env('UPLOADCARE_SECRET_KEY'),
}

# Redactor
# =====================================

REDACTOR_OPTIONS = {
    'lang': 'en',
    'plugins': ['uploadcare'],
    'uploadcare': {
        'publicKey': UPLOADCARE['pub_key'],
        'crop': 'free',
        'tabs': 'all',
    }
}

REDACTOR_UPLOAD = 'uploads/'

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
