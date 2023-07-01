from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'humedad',views.HumedadViewSet)
router.register(r'planta',views.PlantaViewSet)
router.register(r'usuario', views.UsuarioViewSet)
urlpatterns = [
   path('', include(router.urls))

]