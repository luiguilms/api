from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'humedad', views.HumedadViewSet, basename='humedad')
router.register(r'planta', views.PlantaViewSet, basename='planta')
router.register(r'usuario', views.UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('', include(router.urls))
]