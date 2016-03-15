from django.test import TestCase
from django.utils.six import StringIO
from django.core.management import call_command
from models import Table01, Table02, Table03
from generic.models import Table_01, Table_02, Table_03, Table_04


class CommandsTest(TestCase):

    def setUp(self):
        self.out = StringIO()

        p1 = Table01.objects.create(nome="row01tb01")
        r1 = Table02.objects.create(nome="row01tb02")
        Table03.objects.create(nome="row01tb03", dono=p1, raca=r1)

        t11 = Table_01.objects.create(nome="row1table1")
        t21 = Table_02.objects.create(nome="row1table2")
        Table_03.objects.create(nome="row1table3", rel1=t11, rel2=t21)
        Table_04.objects.create(nome="row1table4")

    def test_saveall_command(self):
        call_command('saveall', 'saveall.Table01', stdout=self.out)
        self.assertIn('All instances saved.', self.out.getvalue())

    def test_saveall_command_all_option(self):
        call_command('saveall', all=True, stdout=self.out)
        self.assertIn('All instances from all models saved.', self.out.getvalue())

    def test_saveall_command_app_option(self):
        call_command('saveall', app='saveall', stdout=self.out)
        self.assertIn('All instances from all models in "saveall" saved.', self.out.getvalue())

    def test_saveall_command_app_option_doesnt_exist(self):
        call_command('saveall', app='aeho', stdout=self.out)
        self.assertIn("Can't find 'aeho' app.", self.out.getvalue())

    def test_saveall_command_multiple_models(self):
        call_command('saveall', 'saveall.Table01', 'saveall.Table02', stdout=self.out)
        self.assertIn('All instances saved.', self.out.getvalue())

    def test_saveall_command_table_doesnt_exist(self):
        call_command('saveall', 'saveall.wrongtable', stdout=self.out)
        self.assertIn("Can't find 'saveall.wrongtable' model.", self.out.getvalue())
