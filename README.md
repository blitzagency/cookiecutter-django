# CookieCutter Django

## Docs

- [CookieCutter](https://github.com/audreyr/cookiecutter)
- [Template README]({{cookiecutter.project_slug}}/README.md)

## Usage

```bash
# Install cookiecutter
pip install cookiecutter

# Change directories to where you keep your projects
cd path/to/your/projects

# Run cookiecutter template
# Outputs a directory that matches the value you enter for `project_slug`
cookiecutter https://github.com/blitzagency/cookiecutter-django
```

## Develop

1. Clone this repository locally
2. Make your changes
3. __Test your changes__!!! (see below)
4. Commit changes, see: [CONTRIBUTING.md](.//{{cookiecutter.project_slug}}/CONTRIBUTING.md)

__Output Local Copy__:

```bash
# This outputs a built version of this template into ./build
make build

cd ./build/{{ project_slug }}
```

- To spin up the project follow the instructions in the [project README.md]({{cookiecutter.project_slug}}/README.md).

## Automate

```bash
# To see latest help message run
make help
```
