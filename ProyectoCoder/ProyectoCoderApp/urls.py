from django.urls import path

from .views import *

urlpatterns = [
    # URLS de ProyectoCoderApp
    path('', inicio, name="inicio"),

    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('cursos/', cursos, name="cursos"),
    path('crear_curso/', crear_curso, name="crear_curso"),
    path('buscar_comision/', buscar_comision, name="buscar_comision"),
    
    path('entregables/', entregables, name="entregables"),
    # path('base/', base),
]