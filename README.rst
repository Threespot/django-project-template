=============================================
Welcome to the {{ project_name }} project
=============================================

This project uses Django 1.5.1.

Locations of important files:

* ``project_name/`` Django project and apps
* ``docs/`` - project documentation (Sphinx)
* ``requirements/ - project dependencies
* ``static/`` - static media
* ``templates/`` - project HTML templates

Getting Started
-----------------

The following will help you get a development environment up and running::

    ?> virtualenv --distribute {{ project_name }}_env
    ?> cd {{ project_name }}_env
    ?> source ../bin/activate
    ?> git clone git@github.com:Threespot/{{ project_name }}.git
    ?> cd {{ project_name }}
    ?> pip install -r requirements/base.txt
    ?> pip install -r /requirements/development.txt
    ?> ./manage.py syncdb
    ?> ./manage.py runserver

`Read more <http://apps.threespot.com/Threespot-Django-Manual/>`_ about how Threespot does Django.