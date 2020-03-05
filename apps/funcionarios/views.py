from django.shortcuts import render
from django.http import HttpResponse
from .models import Funcionario
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


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


def pdf_reportlab(request):
    respose = HttpResponse(content_type='application/pdf')
    respose['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    palavras = ['palavra1', 'palavra2', 'palavra3']

    y = 790
    for palavra in palavras:
        p.drawString(10, y, palavra)
        y-= 40
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    respose.write(pdf)
    return respose