from django.db import models

from conformado.models import Conformado
from proyectos.models import Proyectos


# Create your models here.
class Area(models.Model):
    nombre = models.CharField(max_length=256)
    mision = models.CharField(max_length=256)
    vision = models.CharField(max_length=256)
    proyectos = models.ForeignKey(
       Proyectos, on_delete=models.SET_NULL, null=True)
    conformado = models.ForeignKey(
        Conformado, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"El {self.nombre} tiene como mision {self.mision} y vision {self.vision}"
