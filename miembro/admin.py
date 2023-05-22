from django.contrib import admin

from area.models import Area
from centro_cultural.models import CentroCultural
from comentarios.models import Comentarios
from conformado.models import Conformado
from junta.models import Junta
from miembro.models import Miembro
from miembroxprojecto.models import Miembroxprojecto
from proyectos.models import Proyectos
from publicacion.models import Publicacion
from reacciones.models import Reacciones
from realiza.models import Realiza


# Register your models here.

admin.site.register(Area)
admin.site.register(CentroCultural)
admin.site.register(Comentarios)
admin.site.register(Conformado)
admin.site.register(Junta)
admin.site.register(Miembroxprojecto)
admin.site.register(Miembro)
admin.site.register(Proyectos)
admin.site.register(Publicacion)
admin.site.register(Reacciones)
admin.site.register(Realiza)







# admin.site.register(Domicilio)