from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'tienda/index.html')

def carro(request):
    return render(request,'tienda/carro.html')

def galeria(request):
    return render(request,'tienda/galeria.html')

def login(request):
    return render(request,'tienda/login.html')

def registro(request):
    return render(request,'tienda/registro.html')

def tecnicas(request):
    return render(request,'tienda/tecnicas.html')

def catalogo(request):
    return render(request,'tienda/catalogo.html')