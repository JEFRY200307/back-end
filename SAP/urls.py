"""SAP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


# Para hacer uso del metodo bienvenido(), es necesario importarlo
from home.views import *
from miembro.views import actualizarUsuario, agregarUsuario, descrpcionUser, eliminarUsuario
from proyectos.views import descripcionProyecto, agregarProyecto, actualizarProyecto, eliminarProyecto
from publicacion.views import descripcionPublicacion

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", portada, name="index"),
    
    path("descripcion/<int:id>", descrpcionUser),
    
    path("agregar", agregarUsuario),
    path("actualizar/<int:id>", actualizarUsuario),
    path("eliminar/<int:id>", eliminarUsuario),

    path("agregarproyecto", agregarProyecto),
    path("descripcionproyecto/<int:id>", descripcionProyecto),
    path("actualizarproyecto/<int:id>", actualizarProyecto),
    path("eliminarproyecto/<int:id>", eliminarProyecto),

    path("descripcionpublicacion<int:id>", descripcionPublicacion)
]
