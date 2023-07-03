from django.shortcuts import render
from django.http import HttpResponse
# from django.db.models import Q

from jugadores.models import Jugador


def index(request):
    params = {"nombre_sitio": "All sports"}
    params["jugadores"] = get_jugadores()

    return render(request, 'jugadores/index.html', params)


def get_jugadores():
    return Jugador.objects.all()
