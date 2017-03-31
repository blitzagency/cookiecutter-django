from django.conf.urls import url
from django.views import defaults as default_views
from . import views


urlpatterns = [
    url(r"^$", views.HomeView.as_view(), name="home"),
    url(r"^400/$", default_views.bad_request,
        kwargs={"exception": Exception("Bad Request!")}),
    url(r"^403/$", default_views.permission_denied,
        kwargs={"exception": Exception("Permission Denied")}),
    url(r"^404/$", default_views.page_not_found,
        kwargs={"exception": Exception("Page not Found")}),
    url(r"^500/$", default_views.server_error),
]
