from django.db import models

class Funcionario(models.Model):
    nome_funcionario = models.CharField('Nome', max_length=100)
    cpf = models.CharField('Nome', max_length=14)
    data_nasc = models.DateField()

    def __str__(self):
        return self.nome_funcionario


class Peca(models.Model):
    nome_peca = models.CharField('Nome', max_length=100)
    categoria = models.CharField('Categoria', max_length=100)
    cor = models.CharField('Cor', max_length=100)
    tamanho = models.CharField('Tamanho', max_length=100)
    doador = models.CharField('Doador', max_length=100)

    def __str__(self):
        return self.nome_peca


class AgendaVisita(models.Model):
    data_visita = models.DateField()
    nome_escola = models.ForeignKey('cadastro.Escola', verbose_name='Escola', on_delete=models.CASCADE)
    nome_funcionario = models.ForeignKey('cadastro.Funcionario', verbose_name='Funcionário', on_delete=models.CASCADE)
    qtd_pessoas = models.IntegerField()
    responsavel_agendamento = models.CharField('Responsável', max_length=100)
    turma = models.CharField('Turma', max_length=45)

    def __str__(self):
        return self.data_visita


class Escola(models.Model):
    nome_escola = models.CharField('Escola', max_length=100)
    telefone_escola = models.CharField('Telefone', max_length=9)
    nome_responsavel = models.CharField('Responsavel', max_length=50)

    def __str__(self):
        return self.nome_escola