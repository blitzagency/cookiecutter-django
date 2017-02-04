import re
from django.db import models
from redactor.fields import RedactorField
from pyuploadcare.dj.models import ImageField
from mezzanine.core.models import Displayable


class PageBase(models.Model):

    class Meta:
        abstract = True


class Settings(models.Model):
    phone = models.CharField(max_length=250)
    fax = models.CharField(max_length=250)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    city_state_zip = models.CharField(max_length=250)

    facebook_link = models.URLField(max_length=250, blank=True, null=True)
    twitter_link = models.URLField(max_length=250, blank=True, null=True)
    linked_in_link = models.URLField(max_length=250, blank=True, null=True)
    sort_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
        ordering = ('sort_order', )

    def phone_code(self):
        return re.sub('[^\d]', '', self.phone)


# HOME PAGE
class Home(PageBase):

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Page"


# CONTACT US PAGE
class ContactUs(PageBase):

    class Meta:
        verbose_name = "Contact Us Page"
        verbose_name_plural = "Contact Us Page"
