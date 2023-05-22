from django.shortcuts import render
from django.http import HttpResponse

from miembro.models import Miembro
from proyectos.models import Proyectos
from publicacion.models import Publicacion

# Create your views here.


def bienvenido(request):
    return HttpResponse("Wellcome XD")

def portada(request):
    # Se hara uso del manejador o atributo objects para poder extraer informacion de
    # una clase de modelos creada
    # Para luego llamar a un metodo
    num_miembros = Miembro.objects.count()  # Metodo count: cuenta la cantidad de registros
    list_miembros = Miembro.objects.all()  # Metodo all(): musetra todos los registros (objetos de la clase Users)
    list_proyectos = Proyectos.objects.all()
    list_publicacion = Publicacion.objects.all()
    return render(request, 'bienvenida.html', {'list_miembros': list_miembros, 'num_miembros': num_miembros, 'list_proyectos':list_proyectos, 'list_publicacion':list_publicacion})
