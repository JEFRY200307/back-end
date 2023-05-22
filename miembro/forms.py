from django.forms import ModelForm

from miembro.models import Miembro


class MiClase_MiembroFormulario(ModelForm):
    class Meta:
        model = Miembro
        fields = '__all__'