import datetime

from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Curso
from .forms import NuevoCurso
from django.db.models import Q

# Create your views here.

def inicio(request):

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]

    return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas})

def crear_curso(request):

    # post
    if request.method == "POST":

        formulario = NuevoCurso(request.POST)

        if formulario.is_valid():

            info_curso = formulario.cleaned_data
        
            curso = Curso(nombre=info_curso["nombre"], comision=info_curso["comision"])
            curso.save() # guardamos en la bd
            
            return redirect("cursos")

        else:

            return render(request,"ProyectoCoderApp/formulario_curso.html",{"form":formulario})
    

    else: # get y otros

        formularioVacio = NuevoCurso()

        return render(request,"ProyectoCoderApp/formulario_curso.html",{"form":formularioVacio})

def buscar_comision(request):

    if request.method == "POST":

        comision = request.POST["comision"]
        
        comisiones = Curso.objects.filter( Q(nombre__icontains=comision) | Q(comision__icontains=comision) ).values()
        # User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True))

        return render(request,"ProyectoCoderApp/buscar_comision.html",{"comisiones":comisiones})

    else: # get y otros

        comisiones =  []  #Curso.objects.all()
        
        return render(request,"ProyectoCoderApp/buscar_comision.html",{"comisiones":comisiones})

def profesores(request):
    return render(request,"ProyectoCoderApp/profesores.html",{})

def estudiantes(request):
    return render(request,"ProyectoCoderApp/estudiantes.html",{})

def cursos(request):
    # return HttpResponse("Vista de cursos")

    cursos = Curso.objects.all()

    return render(request,"ProyectoCoderApp/cursos.html",{"cursos":cursos})


def base(request):
    return render(request,"ProyectoCoderApp/base.html",{})

def entregables(request):
    return HttpResponse("Vista de entregables")