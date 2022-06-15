from django.urls import path

from .views import *

urlpatterns = [
    # URLS de ProyectoCoderApp
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('cursos/', cursos),
    path('entregables/', entregables),
]