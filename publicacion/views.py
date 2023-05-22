from django.shortcuts import render

from publicacion.models import Publicacion


# Create your views here.
def descripcionPublicacion(request, id):
    desc = Publicacion.objects.get(pk=id)
    return render(request, "descripcionPublicacion.html", {"desc": desc})