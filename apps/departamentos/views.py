from django.shortcuts import render
from django.views.generic import ListView
from .models import Departamento
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class ListDepartamentos(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class CreateDepartamentos(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(CreateDepartamentos, self).form_valid(form)
        
class UpdateDepartamentos(UpdateView):
    model = Departamento
    fields = ['nome']

class DeleteDepartamentos(DeleteView):
    model = Departamento
    success_url = reverse_lazy('profile')