from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from cadastro.forms import AgendaVisitaForm, EscolaForm, FuncionarioForm, PecaForm
from cadastro.models import AgendaVisita, Peca
from django.core.paginator import Paginator


# Create your views here.

class home(TemplateView):
    template_name = 'index.html'


def handler404(request, exception):
    return render(request, '404.html')

def handler500(request):
    return render(request, '500.html')

class cadastrovisitas(TemplateView):
    template_name = 'cadastrovisitas.html'

class catalogacao(TemplateView):
    template_name = 'catalogacao.html'

def agendadas(request):
    data = {}
    #data['db'] = AgendaVisita.objects.all()
    all = AgendaVisita.objects.all()
    paginator = Paginator(all, 10)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'agendadas.html', data)

def catalogadas(request):
    data = {}
    all = Peca.objects.all()
    paginator = Paginator(all, 10)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'catalogadas.html', data)


def form(request):
    data = {}
    data['form'] = AgendaVisitaForm()
    return render(request, 'form.html', data)

def formescola(request):
    data = {}
    data['formescola'] = EscolaForm()
    return render(request, 'formescola.html', data)

def formfuncionario(request):
    data = {}
    data['formfuncionario'] = FuncionarioForm()
    return render(request, 'formfuncionario.html', data)

def formpeca(request):
    data = {}
    data['formpeca'] = PecaForm()
    return render(request, 'formpeca.html', data)
def create(request):
    form = AgendaVisitaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('agendada')

def createescola(request):
    formescola = EscolaForm(request.POST or None)
    if formescola.is_valid():
        formescola.save()
        return redirect('home')

def createfuncionario(request):
    formfuncionario = FuncionarioForm(request.POST or None)
    if formfuncionario.is_valid():
        formfuncionario.save()
        return redirect('home')

def createpeca(request):
    formpeca = PecaForm(request.POST or None)
    if formpeca.is_valid():
        formpeca.save()
        return redirect('catalogadas')
def view(request, pk):
    data = {}
    data['db'] = AgendaVisita.objects.get(pk=pk)
    return render(request, 'view.html', data)

def viewpeca(request, pk):
    data = {}
    data['db'] = Peca.objects.get(pk=pk)
    return render(request, 'viewpeca.html', data)


def edit(request, pk):
    data = {}
    data['db'] = AgendaVisita.objects.get(pk=pk)
    data['form'] = AgendaVisitaForm(instance=data['db'])
    return render(request, 'form.html', data)

def editpeca(request, pk):
    data = {}
    data['db'] = Peca.objects.get(pk=pk)
    data['formpeca'] = PecaForm(instance=data['db'])
    return render(request, 'formpeca.html', data)


def update(request, pk):
    data = {}
    data['db'] = AgendaVisita.objects.get(pk=pk)
    form = AgendaVisitaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('agendada')

def updatepeca(request, pk):
    data = {}
    data['db'] = Peca.objects.get(pk=pk)
    formpeca = PecaForm(request.POST or None, instance=data['db'])
    if formpeca.is_valid():
        formpeca.save()
        return redirect('catalogadas')


def delete(request, pk):
    db = AgendaVisita.objects.get(pk=pk)
    db.delete()
    return redirect('agendada')

def deletepeca(request, pk):
    db = Peca.objects.get(pk=pk)
    db.delete()
    return redirect('catalogadas')
