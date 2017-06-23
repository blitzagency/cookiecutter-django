from django.utils.translation import ugettext_lazy as _
from app.utils.appconf import AppConf, NOT_SET_BUT_REQUIRED


__all__ = ["ui_kit_conf", ]


class UIKitConf(AppConf):
    pass


ui_kit_conf = UIKitConf("UI_KIT_SETTINGS", {
    # "foo": "bar",
    # "baz": NOT_SET_BUT_REQUIRED,
})
