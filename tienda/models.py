from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=12)
    password2 = models.CharField(max_length=12)
    correo=models.EmailField(unique=True)
    telefono=models.CharField(max_length=9)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.CharField(max_length=3)
    nombreProducto = models.CharField(max_length=50)
    descripcionProducto = models.CharField(max_lenght=100)
    precio = models.CharField(max_lenght=8)
    stock = models.CharField(max_lenght=3)