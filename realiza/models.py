from django.db import models

# Create your models here.

class Realiza(models.Model):
    fecha = models.CharField(max_length=256)