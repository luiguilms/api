from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from sistema.models import Humedad, Planta,Usuario,Temperatura
from .serializers import HumedadSerializer, PlantaSerializer,TemperaturaSerializer,UsuarioSerializer

class IndexView(APIView):
    def get(self, request):
        lista_humedad = Humedad.objects.all()
        serializer_humedad = HumedadSerializer(lista_humedad, many=True)
        return Response(serializer_humedad.data)


class HumedadView(generics.ListCreateAPIView):
    queryset = Humedad.objects.all()
    serializer_class = HumedadSerializer


class HumedadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Humedad.objects.all()
    lookup_url_kwarg = 'humedad_id'
    serializer_class = HumedadSerializer


class HumedadViewSet(viewsets.ModelViewSet):
    queryset = Humedad.objects.all()
    serializer_class = HumedadSerializer


class PlantaView(generics.ListCreateAPIView):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer


class PlantaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planta.objects.all()
    lookup_url_kwarg = 'planta_id'
    serializer_class = PlantaSerializer


class PlantaViewSet(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer

class TemperaturaView(generics.ListCreateAPIView):
    queryset = Temperatura.objects.all()
    serializer_class = TemperaturaSerializer


class TemperaturaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Temperatura.objects.all()
    lookup_url_kwarg = 'temperatura_id'
    serializer_class = TemperaturaSerializer


class TemperaturaViewSet(viewsets.ModelViewSet):
    queryset = Temperatura.objects.all()
    serializer_class = TemperaturaSerializer

class UsuarioView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Usuario.objects.all()
    lookup_url_kwarg = 'usuario_id'
    serializer_class = UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
