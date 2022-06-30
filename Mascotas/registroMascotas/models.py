from django.db import models


# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    raza = models.CharField(max_length=40)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre


class Dueño(models.Model):
    mascota = models.ForeignKey(Mascota, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    rut = models.CharField(max_length=15)
    edad = models.IntegerField()
    email = models.CharField(max_length=50)
    domicilio = models.TextField()
    telefono = models.CharField(max_length=20)
    
    def __str__(self) :
        return self.nombre

