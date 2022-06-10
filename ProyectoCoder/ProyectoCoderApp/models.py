from django.db import models
from numpy import require

# Create your models here.
class Estudiante(models.Model):

    # id por defecto
    nombre = models.CharField(max_length=30) # Texto
    apellido = models.CharField(max_length=30) # Texto
    email = models.EmailField(blank=True, null=True) # Email - Opcional


class Curso(models.Model):

    # id por defecto
    nombre = models.CharField(max_length=30) # Texto
    comision = models.IntegerField()


class Profesor(models.Model):

    # id por defecto
    nombre = models.CharField(max_length=30) # Texto
    apellido = models.CharField(max_length=30) # Texto
    email = models.EmailField(blank=True, null=True) # Email - Opcional

    profesion = models.CharField(max_length=30)

