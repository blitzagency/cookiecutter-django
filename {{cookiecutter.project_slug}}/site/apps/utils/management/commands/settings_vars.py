from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = "Prints settings vars values corresponding to passed args"

    def add_arguments(self, parser):
        parser.add_argument('var_name', type=str)

    def handle(self, *args, var_name=None, **kwargs):
        if var_name:
            if hasattr(settings, var_name):
                self.stdout.write(getattr(settings, var_name))

        # for arg in args:
        #     if hasattr(settings, arg):
        #         self.stdout.write("{}=\"{}\"\n".format(
        #             arg, getattr(settings, arg)))
