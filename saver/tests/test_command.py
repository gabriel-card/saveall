from django.test import TestCase
from django.utils.six import StringIO
from django.core.management import call_command
from saver.models import Pessoa, Animal, Raca
# from generic.models import Table_01, Table_02, Table_03, Table_04


class CommandsTest(TestCase):

    def setUp(self):
        self.out = StringIO()

        p1 = Pessoa.objects.create(nome="Gabriel")
        r1 = Raca.objects.create(nome_raca="Golden")
        Animal.objects.create(nome="Arthas", dono=p1, raca=r1)

        # t11 = Table_01.objects.create(nome="row1table1")
        # t21 = Table_02.objects.create(nome="row1table2")
        # Table_03.objects.create(nome="row1table3", rel1=t11, rel2=t21)
        # Table_04.objects.create(nome="row1table4")

    def test_saveall_command(self):
        call_command('saveall', 'saver.Pessoa', stdout=self.out)
        self.assertIn('All instances saved.', self.out.getvalue())

    def test_saveall_command_all_option(self):
        call_command('saveall', all=True, stdout=self.out)
        self.assertIn('All instances from all models saved.', self.out.getvalue())

    def test_saveall_command_app_option(self):
        call_command('saveall', app=['saver'], stdout=self.out)
        self.assertIn('All instances from all models in "saver" saved.', self.out.getvalue())

    # def test_saveall_command_multiple_apps_option(self):
    #     call_command('saveall', app=['saver', 'generic'], stdout=self.out)
    #     self.assertIn('All instances from all models in "saver, generic" saved.', self.out.getvalue())

    def test_saveall_command_app_option_doesnt_exist(self):
        call_command('saveall', app=['aeho'], stdout=self.out)
        self.assertIn("Can't find 'aeho' app.", self.out.getvalue())

    def test_saveall_command_multiple_models(self):
        call_command('saveall', 'saver.Animal', 'saver.Raca', stdout=self.out)
        self.assertIn('All instances saved.', self.out.getvalue())

    def test_saveall_command_table_doesnt_exist(self):
        call_command('saveall', 'saver.alibaba', stdout=self.out)
        self.assertIn("Can't find 'saver.alibaba' model.", self.out.getvalue())
