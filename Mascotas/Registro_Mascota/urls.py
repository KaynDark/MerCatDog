from django.urls import path, include 
from . import views

urlpatterns = [
    
    # Listar Mascotas
    path('listarMascotas', views.listarMascotas, name ="listarMascotas"),
    
    # Agregar Mascota
    path('agregar_mascota', views.agregar_mascota, name = "agregar_mascota"),
    
    # Editar Mascota
    path('editar_mascota/<str:mascota_nombre>', views.editar_mascota, name = "editar_mascota"),
    
    # Eliminar Mascota
    path('borrar_mascota/<str:mascota_nombre>', views.borrar_mascota, name = "borrar_mascota"),
]