from rest_framework import serializers
from .models import Profesor, Mascota

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'  # O especifica los campos que desees

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'  # O especifica los campos que desees