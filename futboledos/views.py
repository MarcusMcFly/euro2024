# Create your views here.

from django.shortcuts import render, redirect # type: ignore
from .models import Partido, Apuesta, Usuario, Equipo, Resultado, FaseDeGrupos



def lista_partidos(request):
    partidos = Partido.objects.all()
    return render(request, 'lista_partidos.html', {'partidos': partidos})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'lista_equipos.html', {'equipos': equipos})

def lista_apuestas(request):
    apuestas = Apuesta.objects.all()
    return render(request, 'lista_apuestas.html', {'apuestas': apuestas})

def lista_resultados(request):
    resultados = Resultado.objects.all()
    return render(request, 'lista_resultados.html', {'resultados': resultados})

def detalle_partido(request, partido_id):
    partido = Partido.objects.get(pk=partido_id)
    apuestas = Apuesta.objects.filter(partido=partido)
    return render(request, 'detalle_partido.html', {'partido': partido, 'apuestas': apuestas})

def detalle_usuario(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    apuestas = Apuesta.objects.filter(usuario=usuario)
    return render(request, 'detalle_usuario.html', {'usuario': usuario, 'apuestas': apuestas})

def detalle_equipo(request, equipo_id):
    equipo = Equipo.objects.get(pk=equipo_id)
    partidos = Partido.objects.filter(equipo_local=equipo) | Partido.objects.filter(equipo_visitante=equipo)
    return render(request, 'detalle_equipo.html', {'equipo': equipo, 'partidos': partidos})

def detalle_apuesta(request, apuesta_id):
    apuesta = Apuesta.objects.get(pk=apuesta_id)
    return render(request, 'detalle_apuesta.html', {'apuesta': apuesta})

def realizar_apuesta(request, partido_id):
    if request.method == 'POST':
        # Handle the form submission to place an bet
        # Update user's balance and create a new Apuesta instance
        return redirect('detalle_partido', partido_id=partido_id)
    else:
        partido = Partido.objects.get(pk=partido_id)
        return render(request, 'realizar_apuesta.html', {'partido': partido})
    
def detalle_resultado(request, resultado_id):
    resultado = Resultado.objects.get(pk=resultado_id)
    return render(request, 'detalle_resultado.html', {'resultado': resultado})

def editar_resultado(request, resultado_id):
    if request.method == 'POST':
        # Handle the form submission to place an bet
        # Update user's balance and create a new Apuesta instance
        return redirect('detalle_resultado', resultado_id=resultado_id)
    else:
        resultado = Resultado.objects.get(pk=resultado_id)
        return render(request, 'editar_resultado.html', {'resultado': resultado})
    
def borrar_resultado(request, resultado_id):
    if request.method == 'POST':
        # Handle the form submission to place an bet
        # Update user's balance and create a new Apuesta instance
        return redirect('detalle_resultado', resultado_id=resultado_id)
    else:
        resultado = Resultado.objects.get(pk=resultado_id)
        return render(request, 'borrar_resultado.html', {'resultado': resultado})
    

    
def editar_apuesta(request, partido_id):
    if request.method == 'POST':
        # Handle the form submission to place an bet
        # Update user's balance and create a new Apuesta instance
        return redirect('detalle_partido', partido_id=partido_id)
    else:
        partido = Partido.objects.get(pk=partido_id)
        return render(request, 'editar_apuesta.html', {'partido': partido})
    
def borrar_apuesta(request, partido_id):
    if request.method == 'POST':
        # Handle the form submission to place an bet
        # Update user's balance and create a new Apuesta instance
        return redirect('detalle_partido', partido_id=partido_id)
    else:
        partido = Partido.objects.get(pk=partido_id)
        return render(request, 'borrar_apuesta.html', {'partido': partido})
    
def index(request):
    # Your code here
    return render(request, 'index.html')


# views.py


def fase_de_grupos_view(request):
    data = FaseDeGrupos.objects.all()
    return render(request, 'fase_de_grupos.html', {'data': data})



