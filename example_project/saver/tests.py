from django.test import TestCase
from django.utils.six import StringIO
from django.core.management import call_command
from models import Pessoa, Animal, Raca
from generic.models import Table_01, Table_02, Table_03, Table_04


class CommandsTest(TestCase):
    def setUp(self):
        p1 = Pessoa.objects.create(nome="Gabriel")
        r1 = Raca.objects.create(nome_raca="Golden")
        a1 = Animal.objects.create(nome="Arthas", dono=p1, raca=r1)

        t11 = Table_01.objects.create(nome="row1table1")
        t21 = Table_02.objects.create(nome="row1table2")
        t31 = Table_03.objects.create(nome="row1table3", rel1=t11, rel2=t21)
        t41 = Table_04.objects.create(nome="row1table4")

        p1.save()
        r1.save()
        a1.save()
        t11.save()
        t21.save()
        t31.save()
        t41.save()

    def test_saveall_command(self):
        out = StringIO()
        call_command('saveall', 'saver.Pessoa', stdout=out)
        self.assertIn('All instances saved.', out.getvalue())

    def test_saveall_command_all_option(self):
        out = StringIO()
        call_command('saveall', all=True, stdout=out)
        self.assertIn('All instances from all models saved.', out.getvalue())

    def test_saveall_command_app_option(self):
        out = StringIO()
        call_command('saveall', app=['saver'], stdout=out)
        self.assertIn('All instances from all models in "saver" saved.', out.getvalue())

    def test_saveall_command_multiple_apps_option(self):
        out = StringIO()
        call_command('saveall', app=['saver', 'generic'], stdout=out)
        self.assertIn('All instances from all models in "saver, generic" saved.', out.getvalue())

    def test_saveall_command_app_option_doesnt_exist(self):
        out = StringIO()
        call_command('saveall', app=['aeho'], stdout=out)
        self.assertIn("Can't find 'aeho' app.", out.getvalue())

    def test_saveall_command_multiple_models(self):
        out = StringIO()
        call_command('saveall', 'saver.Animal', 'saver.Raca', stdout=out)
        self.assertIn('All instances saved.', out.getvalue())

    def test_saveall_command_table_doesnt_exist(self):
        out = StringIO()
        call_command('saveall', 'saver.alibaba', stdout=out)
        self.assertIn("Can't find 'saver.alibaba' model.", out.getvalue())


class ModelsIntegrityTest(TestCase):
    def setUp(self):
        p1 = Pessoa.objects.create(nome="Gabriel")
        r1 = Raca.objects.create(nome_raca="Golden")
        a1 = Animal.objects.create(nome="Arthas", dono=p1, raca=r1)
        p1.save()
        r1.save()
        a1.save()

    def test_integrity_saveall_command_create_update_datetime(self):
        created = Pessoa.objects.filter(pk=1).values('created')[0]['created']
        old_updated = Pessoa.objects.filter(pk=1).values('updated')[0]['updated']

        call_command('saveall', 'saver.Pessoa', stdout=StringIO())

        new_created = Pessoa.objects.filter(pk=1).values('created')[0]['created']
        new_updated = Pessoa.objects.filter(pk=1).values('updated')[0]['updated']

        self.assertNotEqual(old_updated, new_updated)
        self.assertEqual(created, new_created)
