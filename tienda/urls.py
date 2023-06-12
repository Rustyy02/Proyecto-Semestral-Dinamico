from django.urls import path
from . import views

urlpatterns=[
    path('index', views.index, name='index'),
    path('resumen', views.carro, name='resumen'),
    path('galeria', views.galeria, name='galeria'),
    path('login', views.login, name='login'),
    path('registro', views.registro, name='registro'),
    path('tecnicas', views.tecnicas, name='tecnicas'),
    path('catalogo', views.catalogo, name='catalogo')
]