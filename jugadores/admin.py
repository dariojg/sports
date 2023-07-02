from django.contrib import admin
from .models import Jugador, Estadistica


@admin.register(Jugador)
class JugadoresAdmin(admin.ModelAdmin):
    list_display = [
        "apellido",
        "nombre",
        "club",
        "fecha_nacimiento",
        "posicion",
        "nacionalidad",
    ]
    ordering = ["-apellido"]
    list_filter = (
        "nombre",
        "apellido",
        "club",
        "nacionalidad",
    )
    search_fields = (
        "nombre",
        "apellido",
        "club",
        "nacionalidad",
    )


@admin.register(Estadistica)
class EstadisticaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_estadistca",
        "jugador",
    )
    search_fields = ("jugador",)
    list_filter = ("jugador",)
