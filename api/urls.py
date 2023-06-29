from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'humedad',views.HumedadViewSet,basename='humedad')
router.register(r'planta',views.PlantaViewSet,basename='planta')
router.register(r'usuario', views.UsuarioViewSet,basename='usuario')
urlpatterns = [
    path('',views.IndexView.as_view()),
    path('humedad',views.HumedadView.as_view()),
    path('humedad/<int:humedad_id>',views.HumedadDetailView.as_view()),
    
    path('planta',views.PlantaView.as_view()),
    path('planta/<int:planta_id>',views.PlantaDetailView.as_view()),

    

    path('usuario',views.UsuarioView.as_view()),
    path('usuario/<int:usuario_id>',views.UsuarioDetailView.as_view()),

    path('admin/',include(router.urls))

]