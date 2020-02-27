from django.urls import include
from .views import (
    HoraExtraList,
    #FuncionariosUpdate, 
    #FuncionariosDelete, 
    #FuncionariosCreate
)
from django.urls import path


urlpatterns = [
    path('hora_extra_list', HoraExtraList.as_view(), name='hora_extra_list'),
    #path('funcionarios_create/', FuncionariosCreate.as_view(), name='funcionarios_create'),
    #path('editar/<int:pk>', FuncionariosUpdate.as_view(), name='funcionarios_update'),
    #path('deletar/<int:pk>', FuncionariosDelete.as_view(), name='funcionarios_delete'),
]


