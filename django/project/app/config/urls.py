from django.conf import settings
from django.conf.urls import include, url
from django.views import defaults as default_views
from django.contrib import admin


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
    url(r'^', include('app.ui.urls')),
    url(r'^', include("mezzanine.urls")),
]

# -------------------------------------
# DEBUG URLS
# -------------------------------------

if settings.DEBUG:
    # Per latest django debug toolbar
    # See: http://django-debug-toolbar.readthedocs.io/en/stable/installation.html
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),

        # This allows the error pages to be debugged during development
        url(r"^400/$", default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")}),
        url(r"^403/$", default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")}),
        url(r"^404/$", default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")}),
        url(r'^500/$', default_views.server_error),
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
