from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    edad = models.IntegerField()
    
    def __str__(self):
        return self.nombre