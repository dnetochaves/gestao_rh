from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('ok')

class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']