from rest_framework import serializers
from sistema.models import Planta, Humedad,Usuario

class HumedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Humedad
        fields = '__all__'

class PlantaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Planta
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'





