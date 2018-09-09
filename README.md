 Mock API
===================

The concept of the mock API created using Django Rest Framework.

How to run it
=============

Mock API requires python and django and few other libraries to work.

To install them at first create a virtualenv into the chosen location:

    $ virtualenv -p python3 mockapi

Next activate mockapi venv:

    $ source mockapi/bin/activate

Clone the repository into the chosen location:

    $ git clone git@github.com:Razhelq/MockAPI.git

Now you can install requirements using requirements.txt file from the repository:

    $ pip install -r requirements.txt

Before migrating data you need to also create database, so enter postgres console as superuser and execute:

    $ create database mockapi;

To enable our api and `django_rest_framework` in your project you need to add it to `INSTALLED_APPS` in your projects
`settings.py` file:

    $ INSTALLED_APPS = [
        'rest_framework',
        'api'
    ]

Add your `username and password` to `DATABASES` settings in the `setting.py` file:

    $ DATABASES = {
        'default': {
            'NAME': 'mockapi',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'your_user',
            'PASSWORD': 'your_password',
            'HOST': 'localhost'
        }
    }

Next navigate to the directory with the repository, perform the migration and run the server:

    $ python manage.py migrate
    $ python manage.py runserver
