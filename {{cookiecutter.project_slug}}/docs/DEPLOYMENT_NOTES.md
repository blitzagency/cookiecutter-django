# Deployment Notes



Project specific instructions would be included in this file as well.

-----

# Ensure you are logged in
```
vagrant ssh
heroku login
heroku keys:add
```

# Heroku quick start
- create your heroku app,
- setup the DJANGO_SETTINGS_MODULE to heroku to use the project.settings.prod settings file.
- create a dev db or provision a larger db as necessary
- promote db to be default
- deploy to heroku
- syncdb (this step will require creation of an admin user)
- page should serve


## Heroku Deployment Steps
Ensure you have added `'.herokuapp.com'` to your `ALLOWED_HOSTS` variable in settings.prod, and added your app to `INSTALLED_APPS` in settings.base.
```
git add .
git commit -a -m 'initial commit'
```
If you haven't created the app on Heroku already:
```
heroku create app-name
heroku git:remote -a app-name
```
For naming sake, it's best to rename your heroku remotes to semantic titles like `prod` or `staging`. You can do this easily by running: `git remote rename heroku prod`

*NOTE: Only run this if you are not building a static site* (i.e., your static files will live on S3). If you are deploying a static site or you want to see an initial deploy before any S3 buckets have been procured, make sure you also commit your compiled styles and set `SERVE_STATIC = True` in your settings.
```
heroku config:set DISABLE_COLLECTSTATIC=1
```

```
heroku config:set DJANGO_SETTINGS_MODULE=app.config.settings.prod
heroku addons:create heroku-postgresql:hobby-dev
heroku config:set DISABLE_COLLECTSTATIC=1
heroku config:set PYTHONPATH=/app/django/project:/app/django/project/vendor
git push heroku master
```
`git push prod master` if you renamed your remote
```
heroku run ./manage.py migrate
```


# setup app_info.json
Each heroku environment must have a corresponding entry in app_info.json.  This config file is responsible for defining the heroku app name, corresponding app_env name and git remote name.  This is used in the fab deploy scripts

```
{
	"dev": {
		"heroku_app_name": "app-name-dev",
		"APP_ENV": "heroku_dev",
		"heroku_remote_name": "dev"
	},
	"staging": {
		"heroku_app_name": "app-name-staging",
		"APP_ENV": "heroku_staging",
		"heroku_remote_name": "staging"
	},
	"prod": {
		"heroku_app_name": "app-name",
		"APP_ENV": "heroku",
		"heroku_remote_name": "production"
	}
}
```

# experimental deploy process
[labs-preboot](https://devcenter.heroku.com/articles/labs-preboot/)
