import random
from django.core.management.base import BaseCommand


# Use the system PRNG if possible
try:
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False


class Command(BaseCommand):
    help = "Create a secret key suitable for the Django SECRET_KEY setting."

    def add_arguments(self, parser):
        parser.add_argument(
            "-b", "--bash-compat", action="store_true",
            dest="bash_compat", help="Only allow characters compatible with copy/pasting into bash",
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.get_key(bash_compat=options.get(
                "bash_compat")))

    def get_key(
        self, length=50,
        allowed_chars="abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)",
        bash_compat=True
    ):
        """
        Return a securely generated random string.

        The default length of 12 with the a-z, A-Z, 0-9 character set returns
        a 71-bit value. log_2((26+26+10)^12) =~ 71 bits

        Params:

        length - key length
        allowed_chars - allowed characters in key
        bash_compat - remove characters that cause problems in bash
        """
        if bash_compat:
            # ! caused problems when pasting into terminal
            allowed_chars = allowed_chars.replace("!", "")

        if using_sysrandom:
            return "".join(random.choice(allowed_chars) for i in range(length))

        print("Could not find a secure pseudo-random number generator on your system.")

        return ""
