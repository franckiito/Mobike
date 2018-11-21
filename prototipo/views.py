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