
from rest_framework import  viewsets
from sistema.models import Humedad, Planta,Usuario
from .serializers import HumedadSerializer, PlantaSerializer,UsuarioSerializer

class HumedadViewSet(viewsets.ModelViewSet):
    queryset = Humedad.objects.all()
    serializer_class = HumedadSerializer

class PlantaViewSet(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
