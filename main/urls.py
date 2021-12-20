from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('hello/', views.HelloWorld, name='HelloWorld'),
    path('cliente/', views.Clientes, name='Cliente'),
    path('cliente/<int:id>',views.ClientesView, name = 'ClientesView'),
    path('edit/<int:id>', views.EditaCliente, name= 'EditaCliente'),
    path('delete/<int:id>',views.DeletaCliente, name='DeletaCliente'),
    path('novo-cliente/',views.CriaCliente,name='CriaCliente')
]
