from django.db import models

from miembro.models import Miembro


# Create your models here.

class Miembroxprojecto(models.Model):
    fecha_inicio = models.CharField(max_length=256)
    fecha_fin = models.CharField(max_length=256)
    cargo = models.CharField(max_length=256)
    miembro = models.ForeignKey(
        Miembro, on_delete=models.SET_NULL, null=True)
