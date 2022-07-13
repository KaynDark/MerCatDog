from django.urls import path, include
from . import views

urlpatterns = [
    path('agregarJuguete', views.JugueteCreate.as_view(), name="agregarJuguete"),

    path('juguete_list/', views.JugueteList.as_view(), name='juguete_list'),

    path('borrar_juguete/<int:pk>', views.JugueteDelete.as_view(), name='borrar_juguete'),

    path('juguetes/',  views.juguete_collection , name='juguete_collection'),
    
    path('juguetes/<int:pk>/', views.juguete_element ,name='juguete_element'),

]
