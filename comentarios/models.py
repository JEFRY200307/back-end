from django.db import models

# Create your models here.

class Comentarios(models.Model):
    fecha = models.CharField(max_length=256)
    contenido = models.CharField(max_length=256)