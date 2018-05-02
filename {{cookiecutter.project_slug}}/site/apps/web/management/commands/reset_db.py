from django_extensions.management.commands.reset_db import Command as ResetDBCommand


class Command(ResetDBCommand):
    """
    Override default reset_db to disable system check cycle.
    Since Django 1.9 system checks added some url pattern validation which
    can cause some compatibility when:
    1. urls.py(s) dynamically construct urls from the database
    2. A management command attempts to access the db (such as the base
       command here, django_extensions.reset_db)
    Causing an error like:
    psycopg2.OperationalError: database "<db_name>" is being accessed by other users.
    This command replaces the default django_extensions.reset_db command (through
    the standard "registered last under the same (file) name" way django-admin
    registers commands) and simply sets a fully-documented option
    `requires_system_checks` to False.
    Docs: http://bit.ly/requires_system_checks_docs
    Otherwise, this command simply overrides `handle` to let you know
    you're using a customized version and then forwards everything
    else to super().handle.
    """
    requires_system_checks = False

    def handle(self, *args, **options):
        self.stdout.write(
            "Executing customized version of reset_db that disables system checks.")
        super().handle(*args, **options)
