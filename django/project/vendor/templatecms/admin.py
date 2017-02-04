import json
from django.contrib import admin
from django.conf.urls import url
from django.http import HttpResponse
from django.http import Http404
try:
    from mezzanine.utils.admin import SingletonAdmin
except Exception:
    from mezzanine.core.admin import SingletonAdmin
from . import models
from .utils import get_copy_dict


# TODO consider tearing out this dependancy on mezzanine...

@admin.register(models.Copy)
class CopyAdmin(SingletonAdmin):

    def save_model(self, request, obj, form, change):
        prefix = "copy__"
        post_data = request.POST
        output = {}

        for key in post_data:
            if prefix in key:
                new_key = key.replace(prefix, "")
                if new_key:
                    output[new_key] = post_data[key]
        obj.copy = output
        obj.save()

    def get_urls(self):
        urls = super(CopyAdmin, self).get_urls()
        my_urls = [
            url(r'^api/update/$', self.api_update_view,
                name="templatecms_copy_api_update"),
        ]
        return my_urls + urls

    def api_update_view(self, request):
        if request.method != "POST":
            raise Http404()
        copy_dict = get_copy_dict(skip_cache=True)
        data = json.loads(request.body.decode('utf-8'))

        copy_dict.update(data.get("data", {}))

        copy_model, _ = models.Copy.objects.get_or_create(id=1)
        copy_model.copy = copy_dict
        copy_model.save()

        return HttpResponse(status=200)
