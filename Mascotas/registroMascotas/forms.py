from dataclasses import fields
from tkinter import Widget
from django import forms 
from .models import Mascota, Dueño

class MascotaForm(forms.ModelForm):
    class meta:
        model = Mascota
        fields = ['nombre', 'raza', 'edad']

        labels = {
            'nombre': 'Nombre',
            'raza': 'Raza',
            'edad': 'Edad',
        }

        Widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
        }
