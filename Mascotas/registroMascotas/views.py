from re import template
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from registroMascotas.models import Mascota
from .forms import MascotaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

#------------- importacines API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import MascotaSerializer
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser


# Create your views here.
def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, "registro/listar_mascotas.html", {'mascotas': mascotas})

def agregar_mascota(request):
    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("registro/agregar_mascota")
    else:
        form = MascotaForm
        return render(request, "registro/agregar_mascota.html", {'form': form})


def borrar_mascota(request, nombre_Mascota):
    instancia = Mascota.objects.get(nombre_Mascota)
    instancia.delete()

    return redirect('listar_mascotas')

def editar_mascota(request, nombre_Mascota):
    instancia = Mascota.objects.get(nombre_Mascota)
    form = MascotaForm(instance=instancia)

    if request.method == "POST":
        form = MascotaForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save

    return render(request, "registro/editar_mascota.html", {'form': form})

#     # clases generics
class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'registro/mascota_form.html'
    success_url = reverse_lazy("listar_mascotas")

class MascotaList(ListView):
    model = Mascota
    template_name = 'registro/list_mascota.html'

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'registro/mascota_form.html'
    success_url = reverse_lazy('list_mascota')

class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'registro/borrar_mascota.html'
    success_url = reverse_lazy('list_mascota')


#------------------------- API REST -----------------------
@api_view(['GET', 'POST'])
def mascota_collection(request):
    if request.method == 'GET':
        mascota = Mascota.objects.all()
        serializer = MascotaSerializer(mascota, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = MascotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def mascota_element(request, pk):
    mascota = get_object_or_404(Mascota, id=pk)

    if request.method == 'GET':
        serializer = MascotaSerializer(mascota)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        mascota_new = JSONParser().parse(request) 
        serializer = MascotaSerializer(mascota, data=mascota_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)