from django.test import TestCase
from django.utils.six import StringIO
from django.core.management import call_command
from models import Pessoa, Animal, Raca


class CommandsTest(TestCase):
    def setUp(self):
        p1 = Pessoa(nome="Gabriel")
        r1 = Raca(nome_raca="Golden Retriever")
        a1 = Animal(nome="Arthas", dono=p1, raca=r1)
        p1.save()
        r1.save()
        a1.save()

    def saveAllCommand(self):
        out = StringIO()
        call_command('saveall', stdout=out)
        self.AssertIn('All instances saved.', out.getvalue())
