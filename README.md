# Django-template

This is a complete ready-to-use template for django framework along with some example content to use. It uses Bootstrap for design, Crispy forms for templates and pipenv for package management.

## Features:

- Mobile-ready base template, page menu
- Deployment config: procfile (Heroku), deploy.sh, docker
- User utilities: Login, registration, profile page
- Test user migrations
- About page and privacy policy
- Color schema, configurable with just one variable
- (TBD) Scheduled application and shell script for crontab
- (TBD) Error page with logging config (debug mode)
- (TBD) Example API

## File structure

\> `main`:
This directory includes ready-to-use templates such as about page and privacy policy

\> `myproject`:
Root directory for Django project. Includes settings and URL settings.

\> `templates`:
Includes most basic templates that are used as a parent for other templates. 

\> `users`:
User utilities, such as user registration, login, profile and also data to load test users.

# Instructions

This project is a template, you can use it to start your own project.
If you cannot use template, clone repo locally and add another git remote.

Run server: `pipenv run python manage.py runserver`

To create a superuser: `pipenv run python manage.py createsuperuser`

Before deployment, check for TODOs, they mark what needs to be changed / updated. Privacy policy is just an example and it is not meant to be legally binding.
