from django.forms import modelform_factory
from django.shortcuts import redirect, render
from usuarios.forms import MiClase_UsuarioFormulario

from usuarios.models import Users

# Create your views here.


def descrpcionUser(request, id):
    desc = Users.objects.get(pk=id)
    return render(request, "descripcion.html", {"des": desc})


# ************* Agregar Usuario *************

# Crearemos una clase Django
# UsuarioForm = modelform_factory(Users, exclude=[])


def agregarUsuario(request):
    if request.method == "POST":
        # Creamos un bojeto de la clase UsuarioFormulario para procesar el formulario
        FormUsuario = MiClase_UsuarioFormulario(request.POST)
        if FormUsuario.is_valid:
            FormUsuario.save()
            # Luego retornaremso una redireccion automatica al terminar de llenar el form
            return redirect("index")
    else:
        userform = MiClase_UsuarioFormulario()
    return render(request, "agregarUsuario.html", {"userform": userform})


# ************* Actualizar Usuario *************
def actualizarUsuario(request, id):
    desc = Users.objects.get(pk=id)
    if request.method == "POST":
        # Creamos un bojeto de la clase UsuarioFormulario para procesar el formulario
        FormUsuario = MiClase_UsuarioFormulario(request.POST, instance=desc)
        if FormUsuario.is_valid:
            FormUsuario.save()
            # Luego retornaremso una redireccion automatica al terminar de llenar el form
            return redirect("index")
    else:
        userform = MiClase_UsuarioFormulario(instance=desc)
    return render(request, "actualizar.html", {"userform": userform})
