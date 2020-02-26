from django.shortcuts import render
from django.http import HttpResponse
from .models import Funcionario
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return HttpResponse('Olá')

class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionariosUpdate(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

class FuncionariosDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionarios_list')

class FuncionariosCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionariosCreate, self).form_valid(form)