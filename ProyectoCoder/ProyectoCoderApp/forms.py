from django import forms


class NuevoCurso(forms.Form):

    nombre = forms.CharField(max_length=30,label="Curso")
    comision = forms.IntegerField(min_value=0)

class EstudianteFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)

    email = forms.EmailField()