from __future__ import print_function
import os
import random
import subprocess


# Get the root project directory
# Note: Resolves to path/to/<project_slug>
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


# Use the system PRNG if possible
try:
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False


def get_random_string(
        length=50,
        allowed_chars="abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)"):
    """
    Return a securely generated random string.

    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits
    """
    if using_sysrandom:
        return "".join(random.choice(allowed_chars) for i in range(length))
    print(
        "Cookiecutter Django couldn't find a secure pseudo-random number generator on your system."
        " Please change change your SECRET_KEY variables in conf/settings/local.py and env.example"
        " manually."
    )
    return "CHANGEME!!"


def set_secret_key(setting_file_location):
    # Open locals.py
    with open(setting_file_location) as f:
        file_ = f.read()

    # Generate a SECRET_KEY that matches the Django standard
    SECRET_KEY = get_random_string()

    # Replace "CHANGEME!!!" with SECRET_KEY
    file_ = file_.replace("CHANGEME!!!", SECRET_KEY, 1)

    # Write the results to the locals.py module
    with open(setting_file_location, "w") as f:
        f.write(file_)


def make_secret_key(project_directory):
    """Generate and save random secret key."""
    # Determine the local_setting_file_location
    local_setting = os.path.join(
        project_directory,
        "django/project/app/config/settings/local.py"
    )

    # local.py settings file
    set_secret_key(local_setting)

    env_file = os.path.join(
        project_directory,
        "django/env.dist"
    )

    # env.example file
    set_secret_key(env_file)


def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)


def remove_heroku_files():
    """Remove files needed for heroku if it isn't going to be used."""
    HEROKU_FILES = [
        "Procfile", "runtime.txt", "requirements.txt", "docs/heroku-setup.md",
        "django/app_info.json"
    ]

    for filename in HEROKU_FILES:
        file_name = os.path.join(PROJECT_DIRECTORY, filename)
        remove_file(file_name)


def ensure_git_repo(project_directory):
    is_repo = is_git_repo(project_directory)
    is_repo_root = is_git_repo_root(project_directory)

    if is_repo and not is_repo_root:
        print("Warning: Output dir is inside another git working tree!")
        print("Info: If you are using the template `make build` command testing locally you can ignore this warning.")
        init_git_repo()

    elif not is_repo:
        init_git_repo()

    elif is_repo and is_repo_root:
        raise Exception("{} is already a git repository!".format(project_directory))


def is_git_repo_root(project_directory):
    completed = subprocess.run(["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = str(completed.stdout.strip(), "utf-8")
    return result == str(project_directory)


def is_git_repo(project_directory):
    completed = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = str(completed.stdout.strip(), "utf-8")
    return result == "true"


def init_git_repo():
    subprocess.run(["git", "init"], check=True, stdout=open(os.devnull, "wb"))
    subprocess.run(["git", "add", "-A"], check=True, stdout=open(os.devnull, "wb"))
    subprocess.run(
        ["git", "commit", "-m", "'chore(project): Initial commit'"], check=True,
        stdout=open(os.devnull, "wb")
    )

    print("Info: Initialized git repository")


# Lets do some stuff!!!
# =====================================

# 1. Generates and saves random secret key
make_secret_key(PROJECT_DIRECTORY)

# 2. Removes all heroku files if it isn't going to be used
if "{{ cookiecutter.use_heroku }}".lower() != "y":
    remove_heroku_files()

# 3. Ensure PROJECT_DIRECTORY is a git repository
ensure_git_repo(PROJECT_DIRECTORY)
