from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns = [
    # lista de Mascotas
    path('listarMascotas', views.listar_mascotas, name="listar_mascotas"),

    # Agregar Mascota
    path('agregarMascotas', views.agregar_mascota, name="agregar_mascota"),

    # Editar Mascota
    path('editarMascotas/<int:nombre_id>', views.editar_mascota, name="editar_mascota"),

    # Borrar Mascota
    # path('borrarMascotas/<int:nombre_id>', views.borrar_mascota, name="borrar_mascota"),
    
    # ------------------- Generics -------------------------
    path('add_mascotas', views.MascotaCreate.as_view(), name="add_mascota"),

    path('list_mascotas/', views.MascotaList.as_view(), name='list_mascota'),

    path('edit_mascotas/<int:pk>', views.MascotaUpdate.as_view(), name='edit_mascota'),

    path('del_mascotas/<int:pk>', views.MascotaDelete.as_view(), name='del_mascota'),

    # API
    path('mascotas/',  views.mascota_collection , name='mascota_collection'),
    path('mascotas/<int:pk>/', views.mascota_element ,name='mascota_element')
]
