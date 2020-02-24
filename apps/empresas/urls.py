from django.urls import include
from .views import EmpresaCreate
from .views import EmpresaEdit
from django.urls import path

urlpatterns = [
    path('create_empresa', EmpresaCreate.as_view(), name='create_empresa'),
    path('edite_empresa/<int:pk>', EmpresaEdit.as_view(), name='edite_empresa'),
]
