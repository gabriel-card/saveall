from django.test import TestCase
from django.utils.six import StringIO
from django.core.management import call_command
from saver.models import Pessoa, Animal, Raca


class ModelsIntegrityTest(TestCase):

    def setUp(self):
        self.out = StringIO()
        p1 = Pessoa.objects.create(nome="Gabriel")
        r1 = Raca.objects.create(nome_raca="Golden")
        Animal.objects.create(nome="Arthas", dono=p1, raca=r1)

    def test_integrity_saveall_command_create_update_datetime(self):
        created = Pessoa.objects.filter(pk=1).values('created')[0]['created']
        old_updated = Pessoa.objects.filter(pk=1).values('updated')[0]['updated']

        call_command('saveall', 'saver.Pessoa', stdout=self.out)

        new_created = Pessoa.objects.filter(pk=1).values('created')[0]['created']
        new_updated = Pessoa.objects.filter(pk=1).values('updated')[0]['updated']

        self.assertNotEqual(old_updated, new_updated)
        self.assertEqual(created, new_created)
