from .models import DuenoMascota
from django import forms

class DuenoForm(forms.ModelForm):


    class Meta:
        model = DuenoMascota
        fields = (
            'rut',
            'nombre',
            'telefono',
            'email',
            'direccion',
            'rango_adopcion'
        )
        labels = {
            'rut': 'RUN',
            'nombre': 'Nombre',
            'telefono': 'Numero Telefonico',
            'email': 'Correo electronico',
            'direccion': 'Nombre de la calle/avenida donde vive',
            'rango_adopcion': 'Rango de Adopcion'
        }
        widgets = {
            'rut':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'rango_adopcion':forms.TextInput(attrs={'class':'form-control'})
        }