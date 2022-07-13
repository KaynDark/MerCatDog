from rest_framework import serializers
from .models import Juguete


class JugueteSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Juguete
        fields = ('nombre', 'precio', 'marca')