from django.test import TestCase
from django.utils.six import StringIO
from django.core.management import call_command
from models import Table01, Table02, Table03
from generic.models import Table_01, Table_02, Table_03, Table_04


class ModelsIntegrityTest(TestCase):

    def setUp(self):
        self.out = StringIO()
        self.p1 = Table01.objects.create(nome="row01tb01")
        self.r1 = Table02.objects.create(nome="row01tb02")
        self.a1 = Table03.objects.create(nome="row01tb03", dono=self.p1, raca=self.r1)

        self.t11 = Table_01.objects.create(nome="row1table1")
        self.t21 = Table_02.objects.create(nome="row1table2")
        self.t31 = Table_03.objects.create(nome="row1table3", rel1=self.t11, rel2=self.t21)
        self.t41 = Table_04.objects.create(nome="row1table4")

    def test_integrity_saveall_command_create_update_datetime(self):
        created = Table01.objects.filter(pk=1).values('created')[0]['created']
        old_updated = Table01.objects.filter(pk=1).values('updated')[0]['updated']

        call_command('saveall', 'saveall.Table01', stdout=self.out)

        new_created = Table01.objects.filter(pk=1).values('created')[0]['created']
        new_updated = Table01.objects.filter(pk=1).values('updated')[0]['updated']

        self.assertNotEqual(old_updated, new_updated)
        self.assertEqual(created, new_created)

    def test_unicode_return(self):
        self.assertEqual(self.p1.__unicode__(), "row01tb01")
        self.assertEqual(self.r1.__unicode__(), "row01tb02")
        self.assertEqual(self.a1.__unicode__(), "row01tb03")
        self.assertEqual(self.t11.__unicode__(), "row1table1")
        self.assertEqual(self.t21.__unicode__(), "row1table2")
        self.assertEqual(self.t31.__unicode__(), "row1table3")
        self.assertEqual(self.t41.__unicode__(), "row1table4")
