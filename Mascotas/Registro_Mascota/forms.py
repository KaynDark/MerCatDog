from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'raza', 'edad']

        labels = {
            'nombre': 'Nombre',
            'raza': 'Razas',
            'edad': 'Edad',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
        }