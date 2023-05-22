from django.db import models

# Create your models here.

class Conformado(models.Model):
    cargo = models.CharField(max_length=256)
    fecha_inicio = models.CharField(max_length=256)
    fecha_fin = models.CharField(max_length=256)

    def __str__(self):
        return f"El cargo {self.cargo} tiene {self.fecha_inicio} y {self.fecha_fin}"