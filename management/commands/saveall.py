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
            action='store_true',
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
            try:
                for name in args:
                    self.save_objects(apps.get_models(apps.get_app(name)))
            except ImproperlyConfigured:
                return self.stdout.write("Can't find '%s' app." % args)

            return self.stdout.write('All instances from all models in "%s" saved.' % args)

        try:
            self.save_objects(args)

        except LookupError:
            return self.stdout.write("Can't find '%s' model." % args)

        else:
            self.stdout.write('All instances saved.')

    def save_objects(self, models):
        for model in models:
            if isinstance(model, str):
                objects = apps.get_model(model).objects.all()
            else:
                objects = model.objects.all()

            for obj in objects:
                obj.save()

            self.stdout.write('Successfully saved "%s" instances.' % model)
