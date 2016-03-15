from django.core.management.base import BaseCommand
from django.core.exceptions import ImproperlyConfigured
from django.apps import apps
from optparse import make_option


class Command(BaseCommand):
    args = '<app.model_name app.model_name ...>'
    help = 'Gets all model instances and saves it.'

    option_list = BaseCommand.option_list + (
        make_option(
            '--all',
            action='store_true',
            dest='all',
            default=False,
            help='Gets all instances from all models in project and saves it.'
        ),
        make_option(
            '--app',
            action='store',
            dest='app',
            default=False,
            help='Gets all instances from all models in one or more apps and saves it.'
        ),
    )

    def handle(self, *args, **options):
        if options['all']:
            models = apps.get_models()
            feedback = "All instances from all models saved."

        elif options['app']:
            apps_list = options['app'].split()
            try:
                models_list = []
                for name in apps_list:
                    models_list.append(apps.get_models(apps.get_app(name)))

            except ImproperlyConfigured:
                return self.stdout.write("Can't find '%s' app." % ', '.join(apps_list))

            else:
                models = [item for sublist in models_list for item in sublist]

                feedback = 'All instances from all models in "%s" saved.' % ', '.join(apps_list)

        else:
            try:
                models = []
                for model in args:
                    models.append(apps.get_model(model))

            except LookupError:
                return self.stdout.write("Can't find '%s' model." % args)

            else:
                feedback = 'All instances saved.'

        self.save_objects(models)
        return self.stdout.write(feedback)

    def save_objects(self, models):
        for model in models:
            objects = model.objects.all()

            for obj in objects:
                obj.save()

            self.stdout.write('Successfully saved "%s" instances.' % model)
