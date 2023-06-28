from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

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
    path('login', auth_views.LoginView.as_view(template_name = "login.html"), name='login'),
    path('logout', auth_views.LoginView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




