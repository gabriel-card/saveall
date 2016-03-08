from django.core.management.base import BaseCommand
from saver.models import Pessoa, Raca, Animal

MODELS = [Pessoa, Raca, Animal]


class Command(BaseCommand):
    args = '<model_name model_name ...>'
    help = 'Gets all model instances and saves it.'

    def handle(self, *args, **options):
        if not self.validate_args(args):
            for name in args:
                self.stdout.write('There is no model named "%s".' % name)
            return

        for model in MODELS:
            for names in args:
                for name in names:
                    if name == model.__name__:
                        objects = model.objects.all()

                        for obj in objects:
                            obj.save()

                        self.stdout.write('Successfully saved "%s" instances.' % model)

        self.stdout.write('All instances saved.')

    def validate_args(self, *args):
        for model in MODELS:
            for name in args:
                if name[0] == model.__name__:
                    return True
        return False
