from django.urls import include
from .views import (
    home, 
    FuncionariosList, 
    FuncionariosUpdate, 
    FuncionariosDelete, 
    FuncionariosCreate
)
from django.urls import path
from .views import pdf_reportlab
from .views import Pdf


urlpatterns = [
    path('', home),
    path('funcionarios_list', FuncionariosList.as_view(), name='funcionarios_list'),
    path('funcionarios_create/', FuncionariosCreate.as_view(), name='funcionarios_create'),
    path('editar/<int:pk>', FuncionariosUpdate.as_view(), name='funcionarios_update'),
    path('deletar/<int:pk>', FuncionariosDelete.as_view(), name='funcionarios_delete'),
    path('pdf-reportlab', pdf_reportlab, name='pdf-reportlab'),
    path('relatorio_funcionario_html', Pdf.as_view(), name='relatorio_funcionario_html')
]
