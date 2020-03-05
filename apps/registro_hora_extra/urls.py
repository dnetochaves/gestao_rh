from django.urls import include
from .views import (
    HoraExtraList,
    HoraExtraUpdate, 
    HoraExtraDelete, 
    HoraExtraCreate,
    UtilizouHoraExtra
)

from django.urls import path


urlpatterns = [
    path('list/', HoraExtraList.as_view(), name='hora_extra_list'),
    path('novo/', HoraExtraCreate.as_view(), name='hora_extra_create'),
    path('editar/<int:pk>/', HoraExtraUpdate.as_view(), name='hora_extra_update'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='hora_extra_delete'),
    path('utilizou-hora-extra/<int:pk>/',
         UtilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
]


