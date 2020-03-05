from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
import json


# Create your views here.


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    

class HoraExtraUpdate(UpdateView):
     model = RegistroHoraExtra
     fields = ['motivo', 'funcionario', 'horas']

class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('hora_extra_list')


class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizadas = True
        registro_hora_extra.save()

        funcionario = self.request.user.funcionario

        response = json.dumps(

            {'mensagem': 'Horás marcada com utilizada','horas':float(funcionario.total_horas_extra)}

            )
        
        return HttpResponse(response, content_type='application/json')