.. image:: https://travis-ci.org/gabriel-card/saveall.svg?branch=master
    :target: https://travis-ci.org/gabriel-card/saveall
.. image:: https://coveralls.io/repos/github/gabriel-card/saveall/badge.svg
    :target: https://coveralls.io/r/gabriel-card/saveall

django-saveall
--------------

custom django-admin command for saving model instances throughout a project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Requirements:
^^^^^^^^^^^^^

-  Python == 2.7
-  django == 1.7.7 to 1.8.11

How to install:
^^^^^^^^^^^^^^^

-  Run ``pip install django-saveall``;
-  Add ``'saveall'`` to INSTALLED\_APPS inside your settings.py

How to use:
^^^^^^^^^^^

-  You can call the command using
   ``python manage.py saveall <app.Model>`` or
   ``python manage.py saveall --<option> <args>``;
-  Options available:
-  ``--app <app_name>``: accepts multiple arguments, saves all instances
   from all models inside specific app(s);
-  ``--all``: accepts no arguments, saves all instances from all models
   inside project;

Saving instances from specific models:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  By default, the command accepts as argument the path of the model you
   want the instances to be saved. e.g.:
-  ``python manage.py saveall app01.Model01``
-  It accepts multiple paths as well:
-  ``python manage.py saveall app01.Model01 app02.Model02 app03.Model03``

Saving instances from all models inside an app:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Using the ``--app`` option, the command will accept as argument
   solely the name of the app, and will save every instance from every
   model:
-  ``python manage.py saveall --app app01``
-  It accepts multiple apps as well:
-  ``python manage.py saveall --app app01 app02 app03``

Saving all instances from all models inside a project:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Using the ``--all`` option, the command will get every instance from
   every model inside the whole project and save it. It does not accept
   arguments.
-  ``python manage.py saveall --all``
