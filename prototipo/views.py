from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

# Create your views here.

def index(request):
    return render(request,'index.html')

def admin(request):
    return render(request,'administrador.html')

def login(request):
    return render(request,'admin.html')

def registro(request):
    return render(request,'registro.html')

def usuario(request):
    return render(request,'usuario.html')
    
def arrendador(request):
    return render(request,'arrendador.html')
    
def bicicleta(request):
    return render(request,'bicicleta.html')

def editar_perfil(request):
    return render(request,'editarPerfil.html')

def agregar_bicicleta(request):
    return render(request,'agregarBicicleta.html')
    
def editar_bicicleta(request):
    return render(request,'editarBicicleta.html')

def admin_agregar_bicicleta(request):
    return render(request,'agregarBicicleta1.html')
    
def admin_editar_bicicleta(request):
    return render(request,'editarBicicleta1.html')

def admin_usuario(request):
    return render(request,'mantenedorUsuario.html')

def admin_usuario_agregar(request):
    return render(request,'agregarUsuario.html')

def admin_usuario_editar(request):
    return render(request,'editarUsuario.html')

def reportes(request):
    return render(request,'reportes.html')

def user_login(request):
    return render(request,'login.html')