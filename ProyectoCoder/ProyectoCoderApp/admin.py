from django.contrib import admin

from ProyectoCoderApp.models import Curso

# Register your models here.
class CursoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'comision')

admin.site.register(Curso, CursoAdmin)

# admin, admin -> python manage.py createsuperuser