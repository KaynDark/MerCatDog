from dataclasses import fields
from tkinter import Widget
from django import forms 
from .models import Juguete 

class JugueteForm(forms.ModelForm):
    class meta:
        model = Juguete
        fields = ['nombre', 'precio', 'marca']

        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'marca': 'Marca',
        }

        Widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
        }