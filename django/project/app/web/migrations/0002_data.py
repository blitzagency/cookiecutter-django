# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import migrations


def settings(apps, schema_editor):
    Settings = apps.get_model("app_web", "Settings")
    Settings.objects.create(
        phone="(805) 555-1212",
        fax="(805) 555-1212",
        address1="110 South State Street",
        address2="Suite 200",
        city_state_zip="Camarillo, CA 93010",
        facebook_link="#",
        twitter_link="#",
        linked_in_link="#",
    )


# def home(apps, schema_editor):
#     Home = apps.get_model("sportlogos", "Home")
#     Home.objects.create(
#         # headline="lorem Ipsum",
#     )


# def contact(apps, schema_editor):
#     ContactUs = apps.get_model("sportlogos", "ContactUs")
#     ContactUs.objects.create(
#         # headline="Lorem Ipsum.",
#         # image="https://ucarecdn.com/asdfpoiuqwerkjhasfoiuy234aslkdjh234"
#     )


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(settings),
        # migrations.RunPython(home),
        # migrations.RunPython(contact),
    ]
