from django.conf import settings
from django.conf.urls import include, url
from django.views import defaults as default_views
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin


admin.autodiscover()

urlpatterns = [
    # url(r'^grappelli/', include('grappelli.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^redactor/', include('redactor.urls')),
    # url(r'^', include('sportlogos.urls')),
    # url(r'^', include("mezzanine.urls")),
]
