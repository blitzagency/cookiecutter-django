from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog


admin.autodiscover()


# -------------------------------------
# PROJECT URLS
# -------------------------------------
# See: https://docs.djangoproject.com/en/dev/topics/http/urls/#example

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^', include('app.web.urls')),
    url(r'^', include('app.ui_kit.urls')),
    url(r'^', include("mezzanine.urls")),
]

if settings.AUTO_ENABLE_I18N:
    urlpatterns = i18n_patterns(*urlpatterns)

    urlpatterns += [
        url(r"^jsi18n/$",
            JavaScriptCatalog.as_view(packages=["app.web"]),
            name="javascript-catalog"),
    ]

# -------------------------------------
# DEBUG URLS
# -------------------------------------

if settings.DEBUG:
    # Per latest django debug toolbar
    # See:
    # http://django-debug-toolbar.readthedocs.io/en/stable/installation.html
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),

    ]

if getattr(settings, 'SERVE_STATIC', False) and settings.SERVE_STATIC:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes': False}),
        url(r'^uploads/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
    ]
