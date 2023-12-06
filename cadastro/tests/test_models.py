from django.test import TestCase
from model_mommy import mommy

class FuncionarioTestCase(TestCase):
    def setUp(self):
        self.funcionario = mommy.make('Funcionario')

    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)

class PecaTestCase(TestCase):
    def setUp(self):
        self.peca = mommy.make('Peca')

    def test_str(self):
        self.assertEquals(str(self.peca), self.peca.nome_peca)

class EscolaTestCase(TestCase):
    def setUp(self):
        self.escola = mommy.make('Escola')

    def test_str(self):
        self.assertEquals(str(self.escola), self.escola.nome_escola)

class AgendaVisitaTestCase(TestCase):
    def setUp(self):
        self.agendavisita = mommy.make('AgendaVisita')

    def test_str(self):
        self.assertEquals(str(self.agendavisita), self.agendavisita.data_visita)
