from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import RegistroHoraExtra
from django.http import HttpResponse
from django.urls import reverse_lazy


# Create your views here.


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'horas']

    def form_valid(self, form):
        hora_extra = form.save(commit=False)
        hora_extra.funcionario.id = self.request.user.funcionario.id
        hora_extra.save()
        return super(HoraExtraCreate, self).form_valid(form)

class HoraExtraUpdate(UpdateView):
     model = RegistroHoraExtra
     fields = ['motivo', 'funcionario', 'horas']

class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('hora_extra_list')