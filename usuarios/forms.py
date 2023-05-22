from django.forms import ModelForm

from usuarios.models import Users


class MiClase_UsuarioFormulario(ModelForm):
    
    class Meta:
        model = Users
        fields = '__all__'
        # Widget = {}
        
