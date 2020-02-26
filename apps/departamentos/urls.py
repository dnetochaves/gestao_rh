from django.urls import include
from .views import ListDepartamentos
from .views import CreateDepartamentos
from .views import UpdateDepartamentos
from .views import DeleteDepartamentos
from django.urls import path

urlpatterns = [
    path('list', ListDepartamentos.as_view(), name='list_departamentos'),
    path('departamento_form', CreateDepartamentos.as_view(), name='create_departamentos'),
    path('updtae/<int:pk>/', UpdateDepartamentos.as_view(), name='departamento_updtae'),
    path('delete/<int:pk>/', DeleteDepartamentos.as_view(), name='departamento_delete'),
]
