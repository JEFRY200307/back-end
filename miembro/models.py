from django.db import models

from comentarios.models import Comentarios
from conformado.models import Conformado
from reacciones.models import Reacciones
from realiza.models import Realiza


# Create your models here.

class Miembro(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    correo = models.CharField(max_length=256)
    contraseña = models.CharField(max_length=256)
    red_social = models.CharField(max_length=256)
    conformado = models.ForeignKey(
        Conformado, on_delete=models.SET_NULL, null=True)
    realiza = models.ForeignKey(
        Realiza, on_delete=models.SET_NULL, null=True)
    comentarios = models.ForeignKey(
        Comentarios, on_delete=models.SET_NULL, null=True)
    reacciones = models.ForeignKey(
        Reacciones, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre}, {self.apellido} {self.correo}"