from django.test import TestCase
from django.utils.six import StringIO
from django.core.management import call_command
from models import Pessoa, Animal, Raca


class CommandsTest(TestCase):
    def setUp(self):
        p1 = Pessoa.objects.create(nome="Gabriel")
        r1 = Raca.objects.create(nome_raca="Golden")
        a1 = Animal.objects.create(nome="Arthas", dono=p1, raca=r1)
        p1.save()
        r1.save()
        a1.save()

    def test_saveall_command(self):
        out = StringIO()
        call_command('saveall', 'saver.Pessoa', stdout=out)
        self.assertIn('All instances saved.', out.getvalue())

    def test_saveall_command_multiple_models(self):
        out = StringIO()
        call_command('saveall', 'saver.Animal', 'saver.Raca', stdout=out)
        self.assertIn('All instances saved.', out.getvalue())

    def test_saveall_command_table_doesnt_exist(self):
        out = StringIO()
        call_command('saveall', 'saver.alibaba', stdout=out)
        self.assertIn("Can't find 'saver.alibaba' model.", out.getvalue())
