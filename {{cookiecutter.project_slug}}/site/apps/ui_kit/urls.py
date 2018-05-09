from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^',
        views.DebugRedirectView.as_view(template_name='ui_kit/index.html', redirect_url_name='/'),
        name='ui-kit-index'
    ),
]
