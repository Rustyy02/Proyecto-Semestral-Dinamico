from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=12)
    password2 = models.CharField(max_length=12)
    correo=models.EmailField(unique=True)
    telefono=models.CharField(max_length=9)
    
    def __str__(self):
        return self.nombre