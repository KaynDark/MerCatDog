from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import DueñoForm

# Create your views here.
class RegistroDueño(CreateView):
    model = User
    template_name = "Dueño_Mascota/Dueño_form.html"
    form_class = DueñoForm
    success_url = reverse_lazy('lista_Dueño')
 
 
class DueñoList(ListView):
    model = User
    template_name = 'Dueño_Mascota/lista_Dueño.html'