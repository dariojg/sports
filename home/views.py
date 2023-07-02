from django.shortcuts import render
from django.http import HttpResponse
# from django.db.models import Q

from .models import CarrouselImage
from jugadores.models import Jugador
from partido.models import Partido


def index(request):
    params = {"nombre_sitio": "All sports"}
    params["jugadores"] = get_jugadores()
    params["proximo_partido"] = get_partido()
    params["images_carrousel"] = get_images_carrousel()
    params["carrousel_main_image"] = CarrouselImage.objects.filter(activado=True)[0]
    return render(request, 'home/index.html', params)


def get_partido():
    proximo_partido = Partido.objects.get(activado=True)
    return proximo_partido


def get_jugadores():
    return Jugador.objects.all()


def get_images_carrousel():
    return CarrouselImage.objects.filter(activado=True)
