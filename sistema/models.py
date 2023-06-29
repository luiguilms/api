from django.db import models

# Create your models here.
class Humedad(models.Model):
    dato = models.IntegerField(default=0)
    pub_date = models.DateTimeField('fecha de registro',auto_now=True)
    
    def __str__(self):
        return str(self.dato)

class Usuario(models.Model):
    usuario = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario

    
class Planta(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('fecha de publicacion',auto_now_add=True)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='planta/', blank=True)
    
    
    def __str__(self):
        return self.nombre