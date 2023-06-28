from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns=[
    path('index', views.index, name='index'),
    path('resumen', views.carro, name='resumen'),
    path('galeria', views.galeria, name='galeria'),
    path('login', views.login, name='login'),
    path('logout', views.logoutUsuario, name='logout'),
    path('registro', views.registro, name='registro'),
    path('tecnicas', views.tecnicas, name='tecnicas'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('registroDjango', views.registroDjango, name='registroDjango'),
    
    #Django
    path('producto-listar', views.productosList, name='productosList'),
    path('producto-agregar', views.productosAdd, name='productosAdd'),
    path('productosMod/<id>/', views.productosMod, name='productosMod'),
    path('producto-eliminar/<id>/', views.productosDel, name='productosDel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




