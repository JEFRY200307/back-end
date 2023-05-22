from django.db import models

# Create your models here.


# Crearemos un modelo que tendra relacion con Users
# En esta oportunidad haremos que el modelo Users tenga dependencia de este nuevo modelo
# Debido a que el modelo Users dependera de este modelo el cual lo llamaremos Domicilio,
# por buena practica el que depdende debe ir despues:


# Creacion de clase no dependiente:

class Domicilio(models.Model):
    calle = models.CharField(max_length=256)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=256)

    def __str__(self):
        return f"ID: {self.id}. Vive en la calle: {self.calle}, N°:{self.no_calle}, pais: {self.pais}"


class Users(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    # Ya que esta clase sera la dependiente, le crearemos una llave foranea:
    domicilio = models.ForeignKey(
        Domicilio, on_delete=models.SET_NULL, null=True)
    # Es necesario pasrale el parametro de on_delete si es que se llegase a aliminar algun registro
    # para que luego no arroje arror.
    # Ademas, debemos pasar el parametro null, con el fin de que la clase pueda aceptar registrps vacios

    # Definimos el metodo __str__() para renombrar el objeto
    def __str__(self):
        return f"Usuario {self.id}: {self.nombre} {self.apellido} {self.email}"
