import datetime
from django.http import HttpResponse

from django.template import Context, Template

def mi_primera_vista(request):

    pass

    return HttpResponse("Saludos desde django en coder")

def segunda_vista(request):

    with open(r"C:\Users\lucas\Documents\CoderHouse\django\ProyectoDjango\MiPrimerProyecto\index.html") as f:
        plantilla = Template(f.read())

    contexto = Context()

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def tiempo(request):

    nombre = "Lucas"
    hoy  = datetime.datetime.now()

    html = f"""
<html>
    <head></head>
    <body>
        <h1>El tiempo es: <h2>{hoy}</h2>  </h1>

        Saludos desde django en <b>coder</b>. Soy {nombre}.
    </body>
</html>"""

    return HttpResponse(html)


def nombre(request,name):

    nombre = name
    hoy  = datetime.datetime.now()

    html = f"""
<html>
    <head></head>
    <body>
        <h1>El tiempo es: <h2>{hoy}</h2>  </h1>

        Saludos desde django en <b>coder</b>. Soy {nombre}.
    </body>
</html>"""

    return HttpResponse(html)

def calcular_edad(request,edad):

    anio_actual = 2022

    anio_nacimiento = anio_actual-edad

    
    html = f"""
<html>
    <head></head>
    <body>
        <h1>Naciste en:</h1>

        El año de nacimiento fue: {anio_nacimiento}
    </body>
</html>"""

    return HttpResponse(html)