from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from . import apps


class UIKitAppHook(CMSApp):
    name = _("UI-Kit")
    app_name = apps.Config.label

    def get_urls(self, page=None, language=None, **kwargs):
        return ["apps.ui_kit.urls", ]


apphook_pool.register(UIKitAppHook)
