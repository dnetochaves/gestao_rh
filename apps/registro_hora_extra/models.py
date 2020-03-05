from django.db import models
from apps.funcionarios.models import Funcionario
from django.shortcuts import reverse

# Create your models here.
class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)
    utilizadas = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('hora_extra_update', args=[self.id])

    def __str__(self):
        return self.motivo
    