from django import forms
from .models import Usuario
from .models import Producto

class agregarForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields='__all__'
        
class productoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'