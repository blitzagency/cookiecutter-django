import logging
from django.conf import settings
from django.views.debug import get_exception_reporter_filter
from django.utils.encoding import force_text
from .slackpy import SlackLogger


log = logging.getLogger(__name__)


class SlackHandler(logging.Handler):

    def format_subject(self, subject):
        """Escape CR and LF characters, and limit length.

        RFC 2822's hard limit is 998 characters per line. So, minus "Subject: "
        the actual subject must be no longer than 989 characters.
        """
        formatted_subject = subject.replace('\n', '\\n').replace('\r', '\\r')
        return formatted_subject[:989]

    def emit(self, record):
        incoming_webhook = None
        channel = None
        username = None

        try:
            incoming_webhook = settings.SLACK_INCOMING_WEB_HOOK
            channel = settings.SLACK_CHANNEL
            username = settings.SLACK_USER_NAME
        except:
            log.info("Slack Logger Disabled")
            return

        logging = SlackLogger(
            incoming_webhook,
            channel,
            username
        )

        method_str = record.levelname.lower()
        method = getattr(logging, method_str)
        try:
            request = record.request
            subject = '%s (%s IP): %s' % (
                record.levelname,
                ('internal' if request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS
                 else 'EXTERNAL'),
                record.getMessage()
            )
            filter = get_exception_reporter_filter(request)
            request_repr = '\n{0}'.format(
                force_text(filter.get_request_repr(request)))
        except Exception:
            subject = '%s: %s' % (
                record.levelname,
                record.getMessage()
            )
            request = None
            request_repr = "unavailable"
        subject = self.format_subject(subject)

        message = "%s" % self.format(record)
        method(message, title="Error Notification")
        message = "Request repr(): %s" % request_repr
        method(message, short=True)