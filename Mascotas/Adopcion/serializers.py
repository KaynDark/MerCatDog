from rest_framework import serializers
from .models import DuenoMascota

class DuenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuenoMascota
        fields = '__all__'