from django import forms
from .models import Usuario

class agregarForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields='__all__'