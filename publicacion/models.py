from django.db import models

from comentarios.models import Comentarios
from reacciones.models import Reacciones
from realiza.models import Realiza


# Create your models here.

class Publicacion(models.Model):
    titulo = models.CharField(max_length=256)
    contenido = models.CharField(max_length=256)
    realiza = models.ForeignKey(
        Realiza, on_delete=models.SET_NULL, null=True)
    comentarios = models.ForeignKey(
        Comentarios, on_delete=models.SET_NULL, null=True)
    reacciones = models.ForeignKey(
        Reacciones, on_delete=models.SET_NULL, null=True)
