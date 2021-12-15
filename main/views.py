from django import http
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Cliente

def HelloWorld(request):
    return HttpResponse('HelloWorld')

def Clientes(request):
    clientes = Cliente.objects.all()
    return render(request,'main/index.html', {'clientes': clientes})

def ClientesView(request,id):
    cliente = get_object_or_404(Cliente, pk=id)
    return render(request,'main/cliview.html',{'cliente':cliente})