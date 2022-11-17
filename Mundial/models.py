from django.db import models

# Create your models here.
class Seleccion(models.Model):

    pais = models.CharField(max_length=40)
    continente = models.CharField(max_length=40)

class Jugador(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)

class Estadio(models.Model):

    nombre = models.CharField(max_length=40)
    capacidad = models.IntegerField()