from django.views.generic import TemplateView


class UiIndexView(TemplateView):
    template_name = "ui/index.html"
