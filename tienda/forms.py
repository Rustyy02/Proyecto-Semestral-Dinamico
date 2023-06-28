from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Usuario, Producto

class registroForm(ModelForm):
    class Meta:
        model=Usuario
        fields=['nombre', 'password', 'correo', 'telefono']
        
class productoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'