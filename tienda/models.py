from django.db import models
from django.forms import DateField


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=12)
    correo=models.EmailField(unique=True)
    telefono=models.CharField(max_length=9)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=50)
    descripcionProducto = models.CharField(max_length=200)
    precio = models.IntegerField(null=True)
    stock = models.CharField(max_length=3)
    imagen = models.ImageField(upload_to='tienda/uploads/', null=True)
    
    def __str__(self):
        return f'{self.nombreProducto} -> {self.precio}'
    
class Boleta(models.Model):
    total = models.IntegerField(null=True)
    fecha = models.DateField(auto_now_add=True)