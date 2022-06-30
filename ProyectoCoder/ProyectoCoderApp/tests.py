from django.test import TestCase

# Create your tests here.
from .models import Curso

class CursoTestCase(TestCase):
    def setUp(self):
        Curso.objects.create(nombre="Curso de Python", comision=1)
        Curso.objects.create(nombre="Curso de Django", comision=2)

    def test_curso_nombre(self):
        curso1 = Curso.objects.get(comision=1)
        self.assertEqual(curso1.nombre, "Curso de Python")

        curso2 = Curso.objects.get(comision=2)
        self.assertEqual(curso2.nombre, "Curso de Django")