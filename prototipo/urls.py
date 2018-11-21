from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name = "index"),
    path('admin',views.admin, name = "admin"),
    path('login',views.login, name = "login"),
    path('registro',views.registro, name = "registro"),
    path('usuario',views.usuario, name = "usuario"),
    path('arrendador',views.arrendador, name = "arrendador"),
    path('bicicleta',views.bicicleta, name = "bicicleta"),
    path('perfil/editar/',views.editar_perfil, name = "editar_perfil"),
    path('bicicleta/agregar/',views.agregar_bicicleta, name = "agregar_bicicleta"),
    path('bicicleta/editar/',views.editar_bicicleta, name = "editar_bicicleta"),
]