from django.db import models

from area.models import Area


# Create your models here.

class Junta(models.Model):
    fecha_inicio = models.CharField(max_length=256)
    fecha_fin = models.CharField(max_length=256)
    area = models.ForeignKey(
        Area, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"La junta: {self.id} empezara el {self.fecha_inicio}, y culminara el {self.fecha_fin}"