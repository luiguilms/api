from rest_framework import serializers
from sistema.models import Planta, Humedad,Usuario,Temperatura

class HumedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Humedad
        fields = ['nombre', 'dato', 'pub_date']

class PlantaSerializer(serializers.ModelSerializer):
    humedad = serializers.PrimaryKeyRelatedField(queryset=Humedad.objects.all())
    temperatura = serializers.PrimaryKeyRelatedField(queryset=Temperatura.objects.all())

    class Meta:
        model = Planta
        fields = ['id', 'humedad','temperatura', 'nombre', 'pub_date']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['usuario', 'contraseña']

class TemperaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperatura
        fields = ['valor']



