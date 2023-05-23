from django.db import models

# Create your models here.
class Contactanos(models.Model):
    correo = models.EmailField()
    nombre = models.CharField(max_length=256)
    telefono = models.IntegerField(max_length=9, blank=True)
    mensajes = models.CharField(max_length=256)



