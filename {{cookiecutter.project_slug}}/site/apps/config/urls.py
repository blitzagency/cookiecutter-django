from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from cms.sitemaps import CMSSitemap


admin.autodiscover()


# -------------------------------------
# PROJECT URLS
# -------------------------------------
# See: https://docs.djangoproject.com/en/dev/topics/http/urls/#example

urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r'^taggit_autosuggest/', include("taggit_autosuggest.urls")),
    url(r"^", include("cms.urls")),
]

if settings.AUTO_ENABLE_I18N:
    urlpatterns = i18n_patterns(*urlpatterns)

    urlpatterns += [
        url(r"^jsi18n/$",
            JavaScriptCatalog.as_view(packages=["app.web"]),
            name="javascript-catalog"),
    ]


# Non-Localized Urls
# =====================================

urlpatterns += [
    url(r"^sitemap\.xml$", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    url(r"^sitemap/", sitemap, {
        "sitemaps": {"cmspages": CMSSitemap},
        "template_name": "web/sitemap.html",
        "content_type": "text/html"
    },
        name="sitemap"
    ),
]

# -------------------------------------
# DEBUG URLS
# -------------------------------------

if settings.DEBUG:
    # Per latest django debug toolbar
    # See:
    # http://django-debug-toolbar.readthedocs.io/en/stable/installation.html
    import debug_toolbar

    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    # Serve media files when DEBUG=True
    urlpatterns = [
        url(
            r"^media/(?P<path>.*)$", serve,
            {"document_root": settings.MEDIA_ROOT, "show_indexes": True}
        ),
    ] + staticfiles_urlpatterns() + urlpatterns
