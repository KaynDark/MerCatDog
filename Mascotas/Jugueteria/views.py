from django.shortcuts import render
from .forms import JugueteForm
from .models import Juguete
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JugueteSerializer
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

class JugueteList(ListView):
    model = Juguete
    template_name = 'Juguete/juguete_list.html'

class JugueteCreate (CreateView):
    model = Juguete
    form_class = JugueteForm
    template_name = 'Jugueteria/juguete_form.html'
    success_url = reverse_lazy('juguete_list')

class JugueteDelete(DeleteView):
    model = Juguete
    template_name = 'Juguete/borrar_juguete.html'
    success_url = reverse_lazy('juguete_list')



@api_view(['GET'])
def juguete_collection(request):
    if request.method == 'GET':
        juguetes = Juguete.objects.all()
        serializer = JugueteSerializer(juguetes, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def juguete_element(request, pk):
    juguete = get_object_or_404(Juguete, id=pk)

    if request.method == 'GET':
        serializer = JugueteSerializer(juguete)
        return Response(serializer.data)