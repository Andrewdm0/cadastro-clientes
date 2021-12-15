from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('hello/', views.HelloWorld, name='HelloWorld'),
    path('cliente/', views.Clientes, name='Cliente'),
    path('cliente/<str:id>',views.ClientesView, name = 'ClientesView'),
]
