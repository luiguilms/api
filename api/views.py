
from rest_framework import  viewsets
from sistema.models import Humedad, Planta,Usuario
from .serializers import HumedadSerializer, PlantaSerializer,UsuarioSerializer

class HumedadViewSet(viewsets.ModelViewSet):
    serializer_class = HumedadSerializer

    def get_queryset(self):
        queryset = Humedad.objects.all()
        dato = self.request.query_params.get('dato', None)
        if dato is not None:
            queryset = queryset.filter(dato=dato)
        return queryset

class PlantaViewSet(viewsets.ModelViewSet):
    serializer_class = PlantaSerializer

    def get_queryset(self):
        queryset = Planta.objects.all()
        nombre = self.request.query_params.get('nombre', None)
        if nombre is not None:
            queryset = queryset.filter(nombre=nombre)
        return queryset

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        queryset = Usuario.objects.all()
        usuario = self.request.query_params.get('usuario', None)
        clave = self.request.query_params.get('clave', None)

        if usuario is not None:
            queryset = queryset.filter(usuario=usuario)
        if clave is not None:
            queryset = queryset.filter(clave=clave)

        return queryset

