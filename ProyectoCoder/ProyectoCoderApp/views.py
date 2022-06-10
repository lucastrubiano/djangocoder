import datetime

from django.shortcuts import render
from django.http import HttpResponse
from httplib2 import Http

from ProyectoCoderApp.models import Curso

# Create your views here.

def inicio(request):

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]

    return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas})

def crear_curso(request):

    # nombre = "Python"
    # comision = 31080

    # nuevo_curso = Curso(nombre=nombre,comision=comision)
    # nuevo_curso.save()

    cursos = Curso()

    lista_cursos = [x.nombre for x in Curso.objects.all()] # para obtener los nombres de los cursos y listarlos

    return HttpResponse(f"Cursos: {str(lista_cursos)}")