"""Entrega1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', mostrar_index, name='index'),
    path('himno/', himno, name='Himno'),
    path('registrar_seleccion/', registrar_seleccion, name='Registrar selección'),
    path('registrar_jugador/', registrar_jugador, name='Registrar jugador'),
    path('registrar_estadio/', registrar_estadio, name='Registrar estadio'),
    path('buscar_seleccion/', buscar_seleccion, name='Buscar selección'),
    path('buscar_jugador/', buscar_jugador, name='Buscar jugador'),
    path('buscar_estadio/', buscar_estadio, name='Buscar estadio'),
]
