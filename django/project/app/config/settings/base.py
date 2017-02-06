"""Common settings and globals."""
import dj_database_url
import environ
from os.path import abspath, basename, dirname, join, normpath

env = environ.Env()

environ.Env.read_env(".env")

# ######### PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)
PROJECT_ROOT = abspath(join(dirname(__file__), '../../../'))

# Site name:
SITE_NAME = basename(DJANGO_ROOT)
GRAPPELLI_ADMIN_TITLE = "project_name"
# ######### END PATH CONFIGURATION


# ######### DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False


# ######### MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('app admin',
     'ryanfabian21@gmail.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# ######### END MANAGER CONFIGURATION


# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://vagrant:vagrant@postgres/vagrant'),
}
# ######### END DATABASE CONFIGURATION


# ######### EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# ######### END EMAIL CONFIGURATION

# ######### CELERY CONFIGURATION
#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# ######### END CELERY CONFIGURATION


# ######### REDIS CONFIGURATION
REDIS_HOST = 'redis://localhost:6379'
# ######### END REDIS CONFIGURATION


# ######### CACHE CONFIGURATION

CACHE_TIMEOUT = env("CACHE_TIMEOUT", default=60 * 60)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': CACHE_TIMEOUT,
    }
}


# ######### END CACHE CONFIGURATION

# ######### GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = "America/Los_Angeles"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# Testing
TEST_RUNNER = 'testing.PytestTestRunner'


# ######### END GENERAL CONFIGURATION


# ######### MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
# ######### END MEDIA CONFIGURATION


# ######### STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = join(PROJECT_ROOT, 'collected-static')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

SERVE_STATIC = False

# See: https://docs.djangoproject.com/en/dev/ref/\
# contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(PROJECT_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/\
# contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# ######### END STATIC FILE CONFIGURATION


# ######### SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = r"f2(!%hox^koxhw%%0a)@@!f5^7lu(1$@es*#1szh2q^@3dejr$"
# ######### END SECRET CONFIGURATION


# ######### SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ('localhost', '127.0.0.1', )
# ######### END SITE CONFIGURATION


# ######### FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/\
# settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(PROJECT_ROOT, 'fixtures')),
)
# ######### END FIXTURE CONFIGURATION


# ######### TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/\
# settings/#template-context-processors
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
# ######### END TEMPLATE CONFIGURATION


# ######### MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE = (
    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # "mezzanine.core.request.CurrentRequestMiddleware",
    # "mezzanine.core.middleware.RedirectFallbackMiddleware",
    # "mezzanine.core.middleware.TemplateForDeviceMiddleware",
    # "mezzanine.core.middleware.TemplateForHostMiddleware",
    # "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    # "mezzanine.core.middleware.SitePermissionMiddleware",
    # "mezzanine.pages.middleware.PageMiddleware",
    # "mezzanine.core.middleware.FetchFromCacheMiddleware",
)
# ######### END MIDDLEWARE CONFIGURATION


# ######### URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'app.config.urls'
# ######### END URL CONFIGURATION


# ######### APP CONFIGURATION
DJANGO_APPS = (
    'app.utils.apps.AppUtilsConfig',
    'grappelli_safe',
    'filebrowser_safe',
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',
    # 'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
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

# Apps specific for this project go here.
LOCAL_APPS = (
    'app.web.apps.AppWebConfig',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
# ######### END APP CONFIGURATION

# ######### WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'app.config.wsgi.application'
# ######### END WSGI CONFIGURATION


# ######### SECURITY CONFIGURATION
USE_HTTPS_FOR_ASSETS = False
# ######### END SECURITY CONFIGURATION


# ######### REQUIRE CONFIGURATION
# The baseUrl to pass to the r.js optimizer.
REQUIRE_BASE_URL = "js"

# The name of a build profile to use for your project, relative to
# REQUIRE_BASE_URL.
# A sensible value would be 'app.build.js'. Leave blank to use the
# built-in default build profile.
REQUIRE_BUILD_PROFILE = "app.build.js"

# The name of the require.js script used by your project,
# relative to REQUIRE_BASE_URL.
# REQUIRE_JS = "vendor/require.js"

# A dictionary of standalone modules to build with almond.js.
# See the section on Standalone Modules, below.
REQUIRE_STANDALONE_MODULES = {}

# Whether to run django-require in debug mode.
# REQUIRE_DEBUG = False

# A tuple of files to exclude from the compilation result of r.js.
# REQUIRE_EXCLUDE = ("build.txt",)

# The execution environment in which to run r.js: node or rhino.
# REQUIRE_ENVIRONMENT = "node"
# ######### END REQUIRE CONFIGURATION


AWS_IS_GZIPPED = True


#  MEZZANINE SPECIFIC
USE_MODELTRANSLATION = False
AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"
INLINE_EDITING_ENABLED = True
SITE_TITLE = GRAPPELLI_ADMIN_TITLE
RICHTEXT_WIDGET_CLASS = 'redactor.widgets.RedactorEditor'


UPLOADCARE = {
    'pub_key': 'demopublickey',
    'secret': 'demoprivatekey',
}


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

# # ADMIN_MENU_ORDER = (
# #     ("SportLogos", (
# #         "sportlogos.Settings",
# #         "sportlogos.Home",
# #         "sportlogos.ContactUs"),
# #      ),
# # )

# SLACK_INCOMING_WEB_HOOK = "https://hooks.slack.com/services/"\
#     "T16K5SQJJ/B16KLM0TB/dTi6sR4LiMsXLJM1GbxOUwJU"
# SLACK_CHANNEL = 'sportlogos-tech'
# SLACK_USER_NAME = 'Logger:LOCAL'


# ####################
# # DYNAMIC SETTINGS #
# ####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())
