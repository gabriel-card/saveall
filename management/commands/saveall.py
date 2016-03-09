from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    args = '<app.model_name app.model_name ...>'
    help = 'Gets all model instances and saves it.'

    def handle(self, *args, **options):
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
