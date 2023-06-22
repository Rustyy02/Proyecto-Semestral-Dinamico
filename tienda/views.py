from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Producto
from .forms import registroForm, productoForm

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
        return render(request, 'tienda/login.html', context)

def tecnicas(request):
    return render(request,'tienda/tecnicas.html')

def catalogo(request):
    return render(request,'tienda/catalogo.html')


def usuariolist(request):
    usuarios= Usuario.objects.all()
    data={
        'usuarios': usuarios
    }
    return render(request,'tienda/usuariolist.html',data)


def usuarioadd(request):
    data={
        'form':agregarForm()
    }
    if request.method == 'POST':
        formulario=agregarForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Usuario guardado"
        else:
            data['form']=formulario
    return render(request,'tienda/usuarioadd.html',data)


def usuariomod(request,id):
    usuario=get_object_or_404(Usuario,id=id)
    
    data={
        'form':agregarForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario=agregarForm(data=request.POST,instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="usuariolist")
        data["form"]=formulario
            
    
    return render(request,'tienda/usuariomod.html',data)

def usuariodel(request,id):
    usuario=get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect(to="usuariolist")

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
            data["mensaje"]="Producto guardado"
        else:
            data['form']=formulario
    return render(request,'tienda/productosAdd.html',data)

def productosMod(request,id):
    producto=get_object_or_404(Producto,id=id)
    
    data={
        'form':productoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario=productoForm(data=request.POST,instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="productosList")
        data["form"]=formulario
        
def productosDel(request,id):
    producto=get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="productosList")

