from django.views.generic import TemplateView


class UiIndexView(TemplateView):
    template_name = "ui_kit/index.html"
