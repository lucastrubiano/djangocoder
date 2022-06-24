import datetime

from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Curso, Profesor
from .forms import NuevoCurso
from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]

    return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas})

"""
def buscar_comision(request):

    if request.method == "POST":

        comision = request.POST["comision"]
        
        comisiones = Curso.objects.filter( Q(nombre__icontains=comision) | Q(comision__icontains=comision) ).values()
        # User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True))

        return render(request,"ProyectoCoderApp/buscar_comision.html",{"comisiones":comisiones})

    else: # get y otros

        comisiones =  []  #Curso.objects.all()
        
        return render(request,"ProyectoCoderApp/buscar_comision.html",{"comisiones":comisiones})
"""

def estudiantes(request):
    return render(request,"ProyectoCoderApp/estudiantes.html",{})



def cursos(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            cursos = Curso.objects.filter( Q(nombre__icontains=search) | Q(comision__icontains=search) ).values()

            return render(request,"ProyectoCoderApp/cursos.html",{"cursos":cursos, "search":True, "busqueda":search})

    cursos = Curso.objects.all()

    return render(request,"ProyectoCoderApp/cursos.html",{"cursos":cursos, "search":False})

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

            return render(request,"ProyectoCoderApp/formulario_curso.html",{"form":formulario,"accion":"Crear Curso"})
    

    else: # get y otros

        formularioVacio = NuevoCurso()

        return render(request,"ProyectoCoderApp/formulario_curso.html",{"form":formularioVacio,"accion":"Crear Curso"})

def eliminar_curso(request, curso_id):

    # post
    curso = Curso.objects.get(id=curso_id)
    curso.delete()

    return redirect("cursos")

def editar_curso(request, curso_id):

    # post
    
    curso = Curso.objects.get(id=curso_id)

    if request.method == "POST":

        formulario = NuevoCurso(request.POST)

        if formulario.is_valid():

            info_curso = formulario.cleaned_data
        
            curso.nombre = info_curso["nombre"]
            curso.comision = info_curso["comision"]
            curso.save() # guardamos en la bd
            
            return redirect("cursos")

            
    formulario = NuevoCurso(initial={"nombre":curso.nombre,"comision":curso.comision})

    return render(request,"ProyectoCoderApp/formulario_curso.html",{"form":formulario,"accion":"Editar Curso"})


def profesores(request):

    profesores = Profesor.objects.all()

    return render(request,"ProyectoCoderApp/profesores.html",{"profesores":profesores})

class ProfesList(ListView):

    model = Profesor
    template_name = "ProyectoCoderApp/profesores_list.html"


class ProfeDetail(DetailView):

    model = Profesor
    template_name = "ProyectoCoderApp/profesor_detail.html"


class ProfeCreate(CreateView):

    model = Profesor
    success_url = "/coderapp/list"#reverse_lazy("profes_list")
    fields = ["nombre", "apellido", "email", "profesion"]

class ProfeUpdate(UpdateView):

    model = Profesor
    success_url = "/coderapp/list"#reverse_lazy("profes_list")
    fields = ["nombre", "apellido", "email", "profesion"]

class ProfeDelete(DeleteView):

    model = Profesor
    success_url = "/coderapp/list"#reverse_lazy("profes_list")

def base(request):
    return render(request,"ProyectoCoderApp/base.html",{})

def entregables(request):
    return HttpResponse("Vista de entregables")