from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def mostrar_index(request):

    return render(request, 'index.html')

def himno(request):

    return render(request, 'himno.html')

def registrar_seleccion(request):

    if request.method == 'POST':
        formulario = FormRegistrarSeleccion(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            seleccion = Seleccion(pais=formulario_limpio['pais'], continente=formulario_limpio['continente'])
            seleccion.save()
            return render(request,'index.html')
    else:
        formulario = FormRegistrarSeleccion()

    return render(request, 'registrar_seleccion.html', {'formulario': formulario})

def registrar_jugador(request):

    if request.method == 'POST':
        formulario = FormRegistrarJugador(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            jugador = Jugador(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], pais=formulario_limpio['pais'])
            jugador.save()
            return render(request,'index.html')
    else:
        formulario = FormRegistrarJugador()

    return render(request, 'registrar_jugador.html', {'formulario': formulario})

def registrar_estadio(request):

    if request.method == 'POST':
        formulario = FormRegistrarEstadio(request.POST)
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            estadio = Estadio(nombre=formulario_limpio['nombre'], capacidad=formulario_limpio['capacidad'])
            estadio.save()
            return render(request,'index.html')
    else:
        formulario = FormRegistrarEstadio()

    return render(request, 'registrar_estadio.html', {'formulario': formulario})

def buscar_seleccion(request):

    if request.GET.get('seleccion', False):
        seleccion = request.GET['seleccion']
        selecciones = Seleccion.objects.filter(pais__icontains=seleccion)
        return render(request, 'buscar_seleccion.html', {'selecciones': selecciones})
    else:
        respuesta = 'No hay datos'

    return render(request, 'buscar_seleccion.html', {'respuesta': respuesta})

def buscar_jugador(request):

    if request.GET.get('jugador', False):
        jugador = request.GET['jugador']
        jugadores = Jugador.objects.filter(apellido__icontains=jugador)
        return render(request, 'buscar_jugador.html', {'jugadores': jugadores})
    else:
        respuesta = 'No hay datos'

    return render(request, 'buscar_jugador.html', {'respuesta': respuesta})

def buscar_estadio(request):

    if request.GET.get('estadio', False):
        estadio = request.GET['estadio']
        estadios = Estadio.objects.filter(nombre__icontains=estadio)
        return render(request, 'buscar_estadio.html', {'estadios': estadios})
    else:
        respuesta = 'No hay datos'

    return render(request, 'buscar_estadio.html', {'respuesta': respuesta})