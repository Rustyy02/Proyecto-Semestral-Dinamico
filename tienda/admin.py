from django.contrib import admin
from .models import Usuario
from .models import Producto

admin.site.register(Usuario)
admin.site.register(Producto)