from django.urls import include
from .views import EmpresaCreate
from django.urls import path

urlpatterns = [
    path('novo', EmpresaCreate.as_view(), name='create_empresa'),
]
