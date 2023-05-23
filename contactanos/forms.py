from django.forms import ModelForm, EmailInput

from contactanos.models import Contactanos


class formContactanos(ModelForm):
    class Meta:
        model = Contactanos
        fields = '__all__'
        widgets = dict(
            correo=EmailInput(attrs={'type': 'email'})
        )





        """widgets = {
            correo=EmailInput(attrs={'type': 'email'})
        }"""
