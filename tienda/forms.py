from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Usuario, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registroForm(ModelForm):
    class Meta:
        model=Usuario
        fields=['nombre', 'password', 'correo', 'telefono']
        
class productoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'
        
class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email','password1','password2']