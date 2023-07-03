
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import  viewsets
from rest_framework.decorators import action
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
    @action(detail=True, methods=['put'])
    def custom_put(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def custom_patch(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['delete'])
    def custom_delete(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlantaViewSet(viewsets.ModelViewSet):
    serializer_class = PlantaSerializer

    def get_queryset(self):
        queryset = Planta.objects.all()
        nombre = self.request.query_params.get('nombre', None)
        if nombre is not None:
            queryset = queryset.filter(nombre=nombre)
        return queryset
    
    @action(detail=True, methods=['put'])
    def custom_put(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def custom_patch(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['delete'])
    def custom_delete(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

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
    
    @action(detail=True, methods=['put'])
    def custom_put(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def custom_patch(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['delete'])
    def custom_delete(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


