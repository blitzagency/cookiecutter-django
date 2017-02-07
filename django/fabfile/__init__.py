import functools

from fabric.api import env, task, run, roles, cd
from fabric.context_managers import shell_env

from .agency_vars import with_vars

from . import vagrant
from . import prod
from . import dev
from . import staging
from .vagrant import runall, killall, resetdb, resetall, test
