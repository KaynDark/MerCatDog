from django.db import models

# Create your models here.

class Juguete(models.Model):
    nombre = models.CharField (max_length=50)
    precio = models.IntegerField()
    marca = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

