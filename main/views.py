from django import http
from django.core import paginator
from django.core.paginator import Page, Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Cliente
from .forms import ClienteForm

def HelloWorld(request):
    return HttpResponse('HelloWorld')

def Clientes(request):
    clientes_lista = Cliente.objects.all().order_by('nome')

    paginator = Paginator(clientes_lista,5)

    page = request.GET.get('page')

    clientes = paginator.get_page(page)

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

def EditaCliente(request,id):
    cliente = get_object_or_404(Cliente,pk=id)
    clienteform = ClienteForm(instance=cliente)

    if(request.method == 'POST'):
        clienteform = ClienteForm(request.POST, instance=cliente)

        if clienteform.is_valid():
            cliente = clienteform.save()
            return redirect('../cliente')
        else:
            return render(request,'main/editacliente.html',{'clienteform':clienteform,'cliente':cliente})

    else:
        return render(request,'main/editacliente.html',{'clienteform':clienteform,'cliente':cliente})

def DeletaCliente(request,id):
    cliente = get_object_or_404(Cliente,pk=id)
    cliente.delete()
    return redirect('../cliente')
