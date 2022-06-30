from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import DuenoMascota
from .forms import DuenoForm

#---------------- IMPORTS API ------------------
from rest_framework import generics
from .serializers import DuenoSerializer
# Create your views here.
# ---------------- token ------------------
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# from django.contrib.auth.models import User


# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
        
# Este código se activa cada vez que se 
# crea un nuevo usuario y se guarda en la base de datos.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class DuenoList(ListView):
    model = DuenoMascota
    template_name = 'Dueño/dueño_list.html'

class DuenoCreate (CreateView):
    model = DuenoMascota
    form_class = DuenoForm
    template_name = 'Dueño/dueño_form.html'
    success_url = reverse_lazy('dueño_list')

class DuenoDelete(DeleteView):
    model = DuenoMascota
    template_name = 'Dueño/borrar_dueño.html'
    success_url = reverse_lazy('dueño_list')


# ------------ API REST ------------------------

class API_objects_details(generics.ListCreateAPIView):
    queryset = DuenoMascota.objects.all()
    serializer_class = DuenoSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = DuenoMascota.objects.all()
    serializer_class = DuenoSerializer