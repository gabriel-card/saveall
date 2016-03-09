from django.core.management.base import BaseCommand
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
            help='Gets all instances from all models and saves it.'
        ),
    )

    def handle(self, *args, **options):
        if options['all']:
            models = apps.get_models()

            for model in models:
                objects = model.objects.all()

                for obj in objects:
                    obj.save()

            return self.stdout.write("All instances from all models saved.")

        try:
            for name in args:
                objects = apps.get_model(name).objects.all()

                for obj in objects:
                    obj.save()

                self.stdout.write('Successfully saved "%s" instances.' % name)

        except LookupError:
            return self.stdout.write("Can't find '%s' model." % name)

        else:
            self.stdout.write('All instances saved.')
