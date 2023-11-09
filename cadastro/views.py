from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from cadastro.forms import AgendaVisitaForm, EscolaForm, FuncionarioForm
from cadastro.models import AgendaVisita
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    return render(request, 'index.html')


class cadastrovisitas(TemplateView):
    template_name = 'cadastrovisitas.html'


class cataloga(TemplateView):
    template_name = 'cataloga.html'


def agendadas(request):
    data = {}
    #data['db'] = AgendaVisita.objects.all()
    all = AgendaVisita.objects.all()
    paginator = Paginator(all, 2)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'agendadas.html', data)


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


def view(request, pk):
    data = {}
    data['db'] = AgendaVisita.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = AgendaVisita.objects.get(pk=pk)
    data['form'] = AgendaVisitaForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = AgendaVisita.objects.get(pk=pk)
    form = AgendaVisitaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('agendada')


def delete(request, pk):
    db = AgendaVisita.objects.get(pk=pk)
    db.delete()
    return redirect('home')
