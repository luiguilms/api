from django.db import models

# Create your models here.
class Humedad(models.Model):
    nombre =models.CharField(max_length=200)
    dato = models.IntegerField(default=0)
    pub_date = models.DateTimeField('fecha de registro',auto_now=True)
    
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario

class Temperatura(models.Model):
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.valor)
    
class Planta(models.Model):
    humedad = models.ForeignKey(Humedad,on_delete=models.CASCADE)
    temperatura = models.ForeignKey(Temperatura, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('fecha de publicacion',auto_now_add=True)
    
    def __str__(self):
        return self.nombre