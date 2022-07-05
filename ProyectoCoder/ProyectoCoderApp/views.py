import datetime

from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Avatar, Curso, Estudiante, Profesor
from .forms import EstudianteFormulario, NuevoCurso
from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import *
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def entrada(request):
    return redirect("inicio")

def inicio(request):

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]
    diccionario = {"nombre":"Juan","apellido":"Perez","edad":20}

    # if request.user.is_authenticated:
    #     # try:
    #     #     avatar = Avatar.objects.get(usuario=request.user)
    #     #     url = avatar.imagen.url
    #     # except:
    #     #     url = "/media/avatar/generica.jpg"
    #     return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas, "url":url})

    return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas})

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")
    
    form = AuthenticationForm()

    return render(request,"ProyectoCoderApp/login.html",{"form":form})

def register_request(request):

    if request.method == "POST":
        
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') # es la primer contraseña, no la confirmacion

            form.save() # registramos el usuario
            # iniciamos la sesion
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")

        return render(request,"ProyectoCoderApp/register.html",{"form":form})

    # form = UserCreationForm()
    form = UserRegisterForm()

    return render(request,"ProyectoCoderApp/register.html",{"form":form})

def logout_request(request):
    logout(request)
    return redirect("inicio")

# vista de editar perfil
@login_required
def editar_perfil(request):

    user = request.user # usuario con el que estamos loggueados

    if request.method == "POST":
        
        form = UserEditForm(request.POST) # cargamos datos llenados

        if form.is_valid():

            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            # user.password = info["password1"]

            user.save()

            return redirect("inicio")


    else:
        form = UserEditForm(initial={"email":user.email, "first_name":user.first_name, "last_name":user.last_name})

    return render(request,"ProyectoCoderApp/editar_perfil.html",{"form":form})

@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
            
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.get(username=request.user.username) # usuario con el que estamos loggueados

            avatar = Avatar(usuario=user, imagen=form.cleaned_data["imagen"])

            avatar.save()

            # avatar = Avatar()
            # avatar.usuario = request.user
            # avatar.imagen = form.cleaned_data["imagen"]
            # avatar.save()

            return redirect("inicio")

    else:
        form = AvatarForm()
    
    return render(request,"ProyectoCoderApp/agregar_avatar.html",{"form":form})

def estudiantes(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            estudiantes = Estudiante.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search) ).values()

            return render(request,"ProyectoCoderApp/estudiantes.html",{"estudiantes":estudiantes, "search":True, "busqueda":search})

    estudiantes = Estudiante.objects.all()

    return render(request,"ProyectoCoderApp/estudiantes.html",{"estudiantes":estudiantes})

def crear_estudiante(request):
    
    # post
    if request.method == "POST":
        
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            estudiante = Estudiante(nombre=info["nombre"],apellido=info["apellido"],email=info["email"])
            estudiante.save()

            return redirect("estudiantes")

        return render(request,"ProyectoCoderApp/formulario_estudiante.html",{"form":formulario})

    # get
    formulario = EstudianteFormulario()
    return render(request,"ProyectoCoderApp/formulario_estudiante.html",{"form":formulario})

def eliminar_estudiante(request,estudiante_id):

    estudiante = Estudiante.objects.get(id=estudiante_id)
    estudiante.delete()

    return redirect("estudiantes")

def editar_estudiante(request,estudiante_id):

    estudiante = Estudiante.objects.get(id=estudiante_id)

    if request.method == "POST":

        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            
            info_estudiante = formulario.cleaned_data
            
            estudiante.nombre = info_estudiante["nombre"]
            estudiante.apellido = info_estudiante["apellido"]
            estudiante.email = info_estudiante["email"]
            estudiante.save()

            return redirect("estudiantes")

    # get
    formulario = EstudianteFormulario(initial={"nombre":estudiante.nombre, "apellido":estudiante.apellido, "email": estudiante.email})
    
    return render(request,"ProyectoCoderApp/formulario_estudiante.html",{"form":formulario})

class EstudiantesList(ListView):

    model = Estudiante
    template_name = "ProyectoCoderApp/estudiantes_list.html"

class EstudianteDetail(DetailView):

    model = Estudiante
    template_name = "ProyectoCoderApp/estudiante_detail.html"

class EstudianteCreate(CreateView):

    model = Estudiante
    success_url = "/coderapp/estudiante/list" # atenciooooooooon!!!! a la primer /
    fields = ["nombre", "apellido", "email"]

class EstudianteUpdate(UpdateView):

    model = Estudiante
    success_url = "/coderapp/estudiante/list" # atenciooooooooon!!!! a la primer /
    fields = ["nombre", "apellido", "email"]

class EstudianteDelete(DeleteView):

    model = Estudiante
    success_url = "/coderapp/estudiante/list" # atenciooooooooon!!!! a la primer /

@staff_member_required
def cursos(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            cursos = Curso.objects.filter( Q(nombre__icontains=search) | Q(comision__icontains=search) ).values()

            return render(request,"ProyectoCoderApp/cursos.html",{"cursos":cursos, "search":True, "busqueda":search})

    cursos = Curso.objects.all()

    return render(request,"ProyectoCoderApp/cursos.html",{"cursos":cursos, "search":False})

@staff_member_required
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

@staff_member_required
def eliminar_curso(request, curso_id):

    # post
    curso = Curso.objects.get(id=curso_id)
    curso.delete()

    return redirect("cursos")

@staff_member_required
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

@login_required
def profesores(request):

    profesores = Profesor.objects.all()

    return render(request,"ProyectoCoderApp/profesores.html",{"profesores":profesores})

class ProfesList(LoginRequiredMixin,ListView):

    model = Profesor
    template_name = "ProyectoCoderApp/profesores_list.html"

class ProfeDetail(DetailView):

    model = Profesor
    template_name = "ProyectoCoderApp/profesor_detail.html"

class ProfeCreate(CreateView):

    model = Profesor
    success_url = "/coderapp/profesores/"#reverse_lazy("profes_list")
    fields = ["nombre", "apellido", "email", "profesion"]

class ProfeUpdate(UpdateView):

    model = Profesor
    success_url = "/coderapp/profesores/"#reverse_lazy("profes_list")
    fields = ["nombre", "apellido", "email", "profesion"]

class ProfeDelete(DeleteView):

    model = Profesor
    success_url = "/coderapp/profesores/"#reverse_lazy("profes_list")

def base(request):
    return render(request,"ProyectoCoderApp/base.html",{})

def entregables(request):
    return HttpResponse("Vista de entregables")