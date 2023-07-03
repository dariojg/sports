from django.shortcuts import render
# from django.http import HttpResponse
# from django.db.models import Q

from .models import CarrouselImage, ImagesHome
from jugadores.models import Jugador
from partido.models import Partido, Formacion


def index(request):
    params = {"nombre_sitio": "All sports"}
    params["img_nav"], params["img_foo"] = get_images()
    params["carrousel_main_image"] = CarrouselImage.objects.filter(activado=True)[0]
    params["images_carrousel"] = get_images_carrousel()
    params["proximo_partido"] = get_partido()
    params["formacion_club_local"] = get_formacion_local_from_partido(params["proximo_partido"])
    params["formacion_club_visitante"] = get_formacion_visitante_from_partido(params["proximo_partido"])
    params["jugadores"] = get_jugadores()

    return render(request, "home/index.html", params)


def get_images():
    footer = ImagesHome.objects.filter(type="footer", activado=True)
    nav = ImagesHome.objects.get(type="nav", activado=True)
    return nav, footer


def get_partido():
    proximo_partido = Partido.objects.get(activado=True)
    return proximo_partido


def get_formacion_local_from_partido(_partido):
    return Formacion.objects.filter(partido=_partido, es_local=True)


def get_formacion_visitante_from_partido(_partido):
    return Formacion.objects.filter(partido=_partido, es_local=False)


def get_jugadores():
    return Jugador.objects.all()


def get_images_carrousel():
    return CarrouselImage.objects.filter(activado=True)
