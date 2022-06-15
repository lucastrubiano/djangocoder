from django.db import models

# Create your models here.

class Curso(models.Model):

    # id por defecto
    nombre = models.CharField(max_length=30) # Texto
    comision = models.IntegerField()


class Estudiante(models.Model):

    # id por defecto
    nombre = models.CharField(max_length=30) # Texto
    apellido = models.CharField(max_length=30) # Texto
    email = models.EmailField(blank=True, null=True) # Email - Opcional


class Profesor(models.Model):

    # id por defecto
    nombre = models.CharField(max_length=30) # Texto
    apellido = models.CharField(max_length=30) # Texto
    email = models.EmailField(blank=True, null=True) # Email - Opcional

    profesion = models.CharField(max_length=30)

class Entregable(models.Model):

    nombre = models.CharField(max_length=30)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()