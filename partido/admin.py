from django.contrib import admin
from .models import Partido, Formacion


@admin.register(Partido)
class JugadoresAdmin(admin.ModelAdmin):
    list_display = ["club_local", "club_visitante", "fecha_partido", "estadio"]
    ordering = ["-fecha_partido"]
    list_filter = ("club_local", "club_visitante", "estadio")
    search_fields = ("club_local", "club_visitante", "estadio")


@admin.register(Formacion)
class EstadisticaAdmin(admin.ModelAdmin):
    list_display = (
        "partido",
        "nombre_jugador",
        "posicion",
    )
    search_fields = (
        "partido",
        "nombre_jugador",
        "posicion",
    )
    list_filter = (
        "partido",
        "nombre_jugador",
        "posicion",
    )
