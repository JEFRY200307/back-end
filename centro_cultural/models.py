from django.db import models

from junta.models import Junta


# Create your models here.

class CentroCultural(models.Model):
    nombre = models.CharField(max_length=256)
    direccion = models.CharField(max_length=256)
    junta = models.ForeignKey(
        Junta, on_delete=models.SET_NULL, null=True)
