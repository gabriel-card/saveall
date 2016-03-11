## django-saveall
###  custom django-admin command for saving model instances throughout a project

Requirements:
* Python == 2.7
* django = 1.7.7

#### How to use:<br>
* You can call the command using `python manage.py saveall <app.model>` or `python manage.py saveall --<option> <args>`;<br><br>

#### Calling instances from specific models:
* By default, the command accepts as argument the path of the model you want the instances to be saved. e.g.:
  * `python manage.py saveall app01.model01`
* It accepts multiple paths as well:
  * `python manage.py saveall app01.model01 app02.model02 app03.model03`

#### Calling all models from an app:
* Using the `--app` option, the command will accept as argument solely the name of the app, and will save every instance from every model:
  * `python manage.py saveall --app app01`
* It accepts multiple apps as well:
  * `python manage.py saveall --app app01 app02 app03`

#### Saving every instance from all models inside a project:
* Using the `--all` option, the command will get every instance from every model inside the whole project and save it. It does not accept arguments.
  * `python manage.py saveall --all`
