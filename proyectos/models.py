from django.db import models

from miembroxprojecto.models import Miembroxprojecto


# Create your models here.

class Proyectos(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_inicio = models.CharField(max_length=256)
    fecha_fin = models.CharField(max_length=256)
    mision = models.CharField(max_length=256)
    vision = models.CharField(max_length=256)
    objetivo = models.CharField(max_length=256)
    espectativa = models.CharField(max_length=256)
    descripcion = models.CharField(max_length=256)
    miembroxprojecto = models.ForeignKey(
        Miembroxprojecto, on_delete=models.SET_NULL, null=True)
