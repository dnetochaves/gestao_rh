from django.urls import include
from .views import ListDepartamentos
from .views import CreateDepartamentos
from django.urls import path

urlpatterns = [
    path('list', ListDepartamentos.as_view(), name='list_departamentos'),
    path('departamento_form', CreateDepartamentos.as_view(), name='create_departamentos'),
]
