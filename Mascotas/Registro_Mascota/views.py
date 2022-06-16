from django.shortcuts import render
from Registro_Mascotas.models import Mascota
from .forms import MascotaForm, redirect


def listarMascotas(request):
    mascotas = Mascota.objects.all()
    return render (request, "Registro_Mascotas/listarMascotas.html", {'mascotas': mascotas})

def agregar_mascota(request):
    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_mascota")
    else:
        form = MascotaForm()
        return render(request, "Registro_Mascotas/agregar_mascota.html", {'form': form})
    
def borrar_mascota(request, mascota_nombre):
    
    instancia = Mascota.objects.get(nombre = mascota_nombre)
    instancia.delete()
    return redirect('listarMascotas')

def editar_mascota(request, mascota_nombre):
    
    instancia = Mascota.objects.get(nombre = mascota_nombre)

    
    form = MascotaForm(instance=instancia)

    if request.method == "POST":
        form = MascotaForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()

    return render(request, "Registro/editar_mascota.html", {'form': form})
