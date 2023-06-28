from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from tienda.Carrito import Carrito
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as login2, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'tienda/index.html')

def carro(request):
    return render(request,'tienda/resumen.html')

def galeria(request):
    return render(request,'tienda/galeria.html')

def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            login2(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Nombre de usuario o contraseña son incorrectos')
            
    context = {}    
    return render(request,'tienda/login.html', context)

def logoutUsuario(request):
    logout(request)
    return redirect ('login')


#########################
def registro(request):
    #### FUNCION NO UTILIZADA
    if request.method != "POST":
        return render(request,'tienda/registro.html')
    else:
        nombre=request.POST["nombre"]
        password=request.POST["password"]
        correo=request.POST["correo"]
        telefono=request.POST["telefono"]
        
        obj=Usuario.objects.create( nombre=nombre,
                                   password=password,
                                   correo=correo,
                                   telefono=telefono)
        obj.save()
        context={'mensaje':"Usuario registrado correctamente"}
        return render(request, 'login', context)
#########################


def registroDjango(request):
    form = CrearUsuarioForm()
    
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get('username')
            messages.success(request, 'Cuenta creada exitosamente para ' + usuario)
            return redirect('login')
            
    context = {'form':form}
    return render(request, 'tienda/registroDjango.html', context)

def tecnicas(request):
    return render(request,'tienda/tecnicas.html')

@login_required(login_url='login')
def catalogo(request):
    
    productos = Producto.objects.all()
    
    return render(request,'tienda/catalogo.html', {'productos': productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect ("catalogo")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect ("catalogo")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect ("catalogo")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect ("catalogo")

##########################################################################
################################PRODUCTOS##########################################

def productosList(request):
    productos= Producto.objects.all()
    data={
        'productos' : productos
    }
    return render(request,'tienda/productosList.html',data)

def productosAdd(request):
    data={
        'form':productoForm()
    }
    if request.method == 'POST':
        formulario=productoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Producto guardado" # type: ignore
        else:
            data['form']=formulario
    return render(request,'tienda/productosAdd.html',data)

def productosMod(request,id):
    producto=get_object_or_404(Producto, id=id)
    data={
        'form':productoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario=productoForm(data=request.POST,instance=producto,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="productosList")
        data["form"]=formulario
    return render(request,'tienda/productosMod.html',data)


def productosDel(request,id):
    producto=get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="productosList")

