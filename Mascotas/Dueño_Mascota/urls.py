from django.urls import path, include
from . import views
from .views import RegistroDueño, DueñoList


urlpatterns = [
    path('registrar', RegistroDueño.as_view(), name="registrar"),
    path('listar', DueñoList.as_view(), name="lista_Dueño"),
]
