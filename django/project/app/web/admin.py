from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
try:
    from mezzanine.utils.admin import SingletonAdmin
except Exception:
    from mezzanine.core.admin import SingletonAdmin
from . import models


@admin.register(models.Settings)
class SettingsAdmin(SingletonAdmin):
    pass


@admin.register(models.Home)
class HomeAdmin(SingletonAdmin):
    pass


@admin.register(models.ContactUs)
class ContactUsAdmin(SingletonAdmin):
    pass
