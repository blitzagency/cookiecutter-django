from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.conf import settings


class DebugRedirectView(TemplateView):
    '''
    Provide a 301 or 302 redirect based on settings.DEBUG.

    View Arguments:
    redirect_url_name -- The 'reverse' url name to redirect to (default 'index')
    permanent         -- Perform a 301 instead of a 302 (default True)

    Usage:
    DebugRedirectView.as_view(
        redirect_url_name='foo',
        permanent=False
    )
    '''
    redirect_url_name = 'index'
    permanent = True

    def dispatch(self, request, *args, **kwargs):
        '''Perform a redirect if DEBUG is set to False.'''
        DEBUG = getattr(settings, 'DEBUG', False)
        if not DEBUG:
            return redirect(self.redirect_url_name, permanent=self.permanent)
        else:
            return super().dispatch(request, *args, **kwargs)
