from django.forms import ModelForm

from proyectos.models import Proyectos


class MiClase_ProyectoFormulario(ModelForm):
    class Meta:
        model = Proyectos
        fields = '__all__'