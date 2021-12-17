from django import http
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Cliente
from .forms import ClienteForm

def HelloWorld(request):
    return HttpResponse('HelloWorld')

def Clientes(request):
    clientes = Cliente.objects.all().order_by('nome')
    return render(request,'main/clientes.html', {'clientes': clientes})

def ClientesView(request,id):
    cliente = get_object_or_404(Cliente, pk=id)
    return render(request,'main/cliview.html',{'cliente':cliente})

def CriaCliente(request):
    if request.method == 'POST':
        clienteform = ClienteForm(request.POST)

        if clienteform.is_valid():
            cliente = clienteform.save()
            return redirect('../cliente')
    else:
        clienteform = ClienteForm()
        return render(request,'main/novo-cliente.html',{'clienteform':clienteform})