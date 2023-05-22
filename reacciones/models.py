from django.db import models

# Create your models here.

class Reacciones(models.Model):
    fecha = models.CharField(max_length=256)
    tipo = models.CharField(max_length=256)