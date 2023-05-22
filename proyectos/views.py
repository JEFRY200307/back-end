from django.shortcuts import render, redirect

from proyectos.forms import MiClase_ProyectoFormulario
from proyectos.models import Proyectos


# Create your views here.
def descripcionProyecto(request, id):
    desc = Proyectos.objects.get(pk=id)
    return render(request, "descripcionProyecto.html", {"desc": desc})


def agregarProyecto(request):
    if request.method == "POST":
        FormUsuario = MiClase_ProyectoFormulario(request.POST)
        if FormUsuario.is_valid:
            FormUsuario.save()
            return redirect("index")
    else:
        userform = MiClase_ProyectoFormulario()
    return render(request, "agregarProyecto.html", {"userform": userform})


def actualizarProyecto(request, id):
    desc = Proyectos.objects.get(pk=id)
    if request.method == "POST":
        FormUsuario = MiClase_ProyectoFormulario(request.POST, instance=desc)
        if FormUsuario.is_valid:
            FormUsuario.save()
            return redirect("index")
    else:
        userform = MiClase_ProyectoFormulario(instance=desc)
    return render(request, "actualizarProyecto.html", {"userform": userform})

def eliminarProyecto(request, id):
    desc = Proyectos.objects.get(pk=id)
    if desc:
        desc.delete()
    return redirect("index")