from django.urls import include
from .views import (
    HoraExtraList,
    HoraExtraUpdate, 
    HoraExtraDelete, 
    HoraExtraCreate
)

from django.urls import path


urlpatterns = [
    path('list/', HoraExtraList.as_view(), name='hora_extra_list'),
    path('novo/', HoraExtraCreate.as_view(), name='hora_extra_create'),
    path('editar/<int:pk>/', HoraExtraUpdate.as_view(), name='hora_extra_update'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='hora_extra_delete'),
]


