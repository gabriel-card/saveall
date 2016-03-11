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
            self.save_objects(apps.get_models())
            return self.stdout.write("All instances from all models saved.")

        if options['app']:
            apps_list = options['app']
            try:
                models_list = []
                for name in apps_list:
                    models_list.append(apps.get_models(apps.get_app(name)))

            except ImproperlyConfigured:
                return self.stdout.write("Can't find '%s' app." % ', '.join(apps_list))

            else:
                for models in models_list:
                    self.save_objects(models)

                return self.stdout.write('All instances from all models in "%s" saved.' % ', '.join(apps_list))

        try:
            models = []
            for model in args:
                models.append(apps.get_model(model))

        except LookupError:
            return self.stdout.write("Can't find '%s' model." % args)

        else:
            self.save_objects(models)
            return self.stdout.write('All instances saved.')

    def save_objects(self, models):
        for model in models:
            objects = model.objects.all()

            for obj in objects:
                obj.save()

            self.stdout.write('Successfully saved "%s" instances.' % model)
