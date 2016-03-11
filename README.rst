=====
saveall
=====

saveall is an app that adds a custom django-admin command for saving model instances throughout a project.

For usage reference, please visit: https://github.com/gabriel-card/saveall

Quick start
-----------

1. Add "saveall" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'saveall',
    )

2. Run `python manage.py migrate` to create the saveall test models.

