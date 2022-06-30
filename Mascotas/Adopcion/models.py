from django.db import models
from django.forms import CharField

# Create your models here.
RANGOS_ADOPCION=(
    ('Aprendiz', 'Aprendiz'),
    ('Conocedor','Conocedor'),
    ('Cuidador','Cuidador'),
    ('Especialista','Especialista'),
)

class DuenoMascota(models.Model):
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=60, blank=True, null=True, unique=True)
    direccion = models.TextField()
    RANGOS_ADOPCION = models.CharField(max_length=50, choices=RANGOS_ADOPCION)

    def __str__(self):
        return self.rut