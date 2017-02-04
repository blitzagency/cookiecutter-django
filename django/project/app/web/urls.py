# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^contact/$', views.ContactView.as_view(), name="contact"),
    url(r'^contact-success/$', views.ContactSuccessView.as_view(),
        name="contact_success"),
    url(r'^404/$', TemplateView.as_view(template_name="404.html")),
    url(r'^500/$', TemplateView.as_view(template_name="500.html")),
]
