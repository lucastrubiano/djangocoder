from django.urls import path

from .views import *

urlpatterns = [
    # URLS de ProyectoCoderApp
    path('', inicio, name="inicio"),

    path('estudiantes/', estudiantes, name="estudiantes"),
    path('crear_estudiante/', crear_estudiante, name="crear_estudiante"),
    path('eliminar_estudiante/<estudiante_id>', eliminar_estudiante, name="eliminar_estudiante"),
    path('editar_estudiante/<estudiante_id>', editar_estudiante, name="editar_estudiante"),

    path('estudiante/list', EstudiantesList.as_view(), name="estudiante_list"),
    path(r'^(?P<pk>\d+)$', EstudianteDetail.as_view(), name="estudiante_detail"),
    path(r'^nuevo$', EstudianteCreate.as_view(), name="estudiante_create"),
    path(r'^editar/(?P<pk>\d+)$', EstudianteUpdate.as_view(), name="estudiante_update"),
    path(r'^eliminar/(?P<pk>\d+)$', EstudianteDelete.as_view(), name="estudiante_delete"),


    
    path('profesores/', profesores, name="profesores"),
    path(r'list', ProfesList.as_view(), name="profe_list"),
    path(r'^(?P<pk>\d+)$', ProfeDetail.as_view(), name="profe_detail"),
    path(r'^nuevo$', ProfeCreate.as_view(), name="profe_create"),
    path(r'^editar/(?P<pk>\d+)$', ProfeUpdate.as_view(), name="profe_update"),
    path(r'^eliminar/(?P<pk>\d+)$', ProfeDelete.as_view(), name="profe_delete"),

    path('cursos/', cursos, name="cursos"),
    path('crear_curso/', crear_curso, name="crear_curso"),
    path('eliminar_curso/<curso_id>/', eliminar_curso, name="eliminar_curso"),
    path('editar_curso/<curso_id>/', editar_curso, name="editar_curso"),
    # path('buscar_comision/', buscar_comision, name="buscar_comision"),
    
    path('entregables/', entregables, name="entregables"),
    # path('base/', base),
]