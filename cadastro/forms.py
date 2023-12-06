from django.forms import ModelForm
from cadastro.models import AgendaVisita, Escola, Funcionario, Peca


class AgendaVisitaForm(ModelForm):
    class Meta:
        model = AgendaVisita
        fields = ['data_visita', 'qtd_pessoas', 'responsavel_agendamento', 'turma', 'nome_escola', 'nome_funcionario']


class EscolaForm(ModelForm):
    class Meta:
        model = Escola
        fields = ['nome_escola', 'telefone_escola', 'nome_responsavel']

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome_funcionario', 'cpf', 'data_nasc']

class PecaForm(ModelForm):
    class Meta:
        model = Peca
        fields = ['nome_peca', 'categoria', 'cor', 'tamanho', 'doador']