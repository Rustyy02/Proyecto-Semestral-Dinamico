from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Producto
from .forms import registroForm, productoForm
from tienda.Carrito import Carrito
from django.contrib.auth.forms import UserCreationForm  

# Create your views here.
def index(request):
    return render(request,'tienda/index.html')

def carro(request):
    return render(request,'tienda/resumen.html')

def galeria(request):
    return render(request,'tienda/galeria.html')

def login(request):
    return render(request,'tienda/login.html')

def registro(request):
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

def registroDjango(request):
    form = UserCreationForm
    context = {'form':form}
    return render(request, 'tienda/registroDjango.html', context)

def tecnicas(request):
    return render(request,'tienda/tecnicas.html')

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

