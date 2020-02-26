from django.views.generic.edit import CreateView, UpdateView
from .models import Documento
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Teste(request):
    return render(request, 'documentos/teste.html')


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
 