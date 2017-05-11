project_slug = "{{ cookiecutter.project_slug }}"
heroku_slug = "{{cookiecutter.heroku_slug}}"


if hasattr(project_slug, "isidentifier"):
    assert project_slug.isidentifier(), "Project slug should be valid Python identifier!"


if heroku_slug:
    assert "_" not in heroku_slug, "Heroku slugs / app names must not have underscores!"
