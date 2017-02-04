from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from . import models
from .forms import ContactForm


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        # context['object'] = models.Home.objects.first()
        return context


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'success': True
            }
            return JsonResponse(data)
        else:
            return response


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm

    def get_context_data(self, *args, **kwargs):
        context = super(ContactView, self).get_context_data(*args, **kwargs)
        # context['object'] = models.ContactUs.objects.first()
        return context

    def form_valid(self, form):
        return super(ContactView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("contact_success")


class ContactSuccessView(TemplateView):
    template_name = "contact_success.html"
