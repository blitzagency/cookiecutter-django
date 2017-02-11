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

## Development & Contributing

1. Clone this repository locally
2. Make your changes
3. Output a project based on the local template (see below)
4. Commit changes, see: [CONTRIBUTING.md](.//{{cookiecutter.project_slug}}/CONTRIBUTING.md)

__Output Local Copy__:

```bash
cookiecutter path/to/local/cookiecutter-django
```
