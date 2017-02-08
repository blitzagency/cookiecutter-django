from django.conf.urls import url
from django.conf import settings
from . import views


if settings.DEBUG:
    urlpatterns = [
        url(r"^ui/$", views.UiIndexView.as_view(), name="ui-index"),
    ]
else:
    urlpatterns = []
