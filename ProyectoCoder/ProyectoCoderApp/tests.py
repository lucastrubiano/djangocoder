from django.test import TestCase

from .models import Curso

# Create your tests here.
class CursosTest(TestCase):
    
    def setUp(self):
        Curso.objects.create(nombre="Curso de Django", comision=2)
        
    def test_curso_nombre(self):
        curso = Curso.objects.get(comision=2)
        self.assertEqual(curso.nombre, "Curso de Django")
    
    def test_curso_creado(self):
        curso = Curso.objects.get(comision=2)
        self.assertNotEquals(curso, None)