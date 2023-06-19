from django.urls import path
from . import views

urlpatterns=[
    path('index', views.index, name='index'),
    path('resumen', views.carro, name='resumen'),
    path('galeria', views.galeria, name='galeria'),
    path('login', views.login, name='login'),
    path('registro', views.registro, name='registro'),
    path('tecnicas', views.tecnicas, name='tecnicas'),
    path('catalogo', views.catalogo, name='catalogo'),
    
    #Django
    path('usuario-listar', views.usuariolist, name='usuariolist'),
    path('usuario-agregar', views.usuarioadd, name='usuarioadd'),
    path('usuario-modificar/<id>/', views.usuariomod, name='usuariomod'),
    path('usuario-eliminar/<id>/', views.usuariodel, name='usuariodel'),
    path('producto-listar', views.productosList, name='productosList'),
    path('producto-agregar', views.productosAdd, name='productosAdd'),
    path('producto-modificar/<id>/', views.productosMod, name='productosMod'),
    path('producto-eliminar/<id>/', views.productosDel, name='productosDel'),
]




