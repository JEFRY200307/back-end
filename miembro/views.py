from django.shortcuts import redirect, render

from miembro.forms import MiClase_MiembroFormulario
from miembro.models import Miembro

# Create your views here.
def descrpcionUser(request, id):
    desc = Miembro.objects.get(pk=id)
    return render(request, "descripcion.html", {"desc": desc})


# ************* Agregar Usuario *************

def agregarUsuario(request):
    if request.method == "POST":
        FormUsuario = MiClase_MiembroFormulario(request.POST)
        if FormUsuario.is_valid:
            FormUsuario.save()
            # Luego retornaremso una redireccion automatica al terminar de llenar el form
            return redirect("index")
    else:
        userform = MiClase_MiembroFormulario()
    return render(request, "agregarMiembro.html", {"userform": userform})


# ************* Actualizar Usuario *************
def actualizarUsuario(request, id):
    desc = Miembro.objects.get(pk=id)
    if request.method == "POST":
        # Creamos un bojeto de la clase UsuarioFormulario para procesar el formulario
        FormUsuario = MiClase_MiembroFormulario(request.POST, instance=desc)
        if FormUsuario.is_valid:
            FormUsuario.save()
            # Luego retornaremso una redireccion automatica al terminar de llenar el form
            return redirect("index")
    else:
        userform = MiClase_MiembroFormulario(instance=desc)
    return render(request, "actualizar.html", {"userform": userform})

def eliminarUsuario(request, id):
    desc = Miembro.objects.get(pk=id)
    if desc:
        desc.delete()
    return redirect("index")