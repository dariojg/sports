from django.db import models


class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="jugadores/", blank=True, null=True)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50, null=True)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)


class Estadistica(models.Model):
    PASES = "Pases"
    GOLES = "Goles"
    PARTIDOS_JUGADOS = "Partidos Jugados"
    PENALES_ACERTADOS = "Penales acertados"
    PENALES_ERRADOS = "Penales errados"
    PENALES_ATAJADOS = "Penales Atajados"
    ESTADISTICA_JUGADOR = (
        (PASES, "Pases"),
        (GOLES, "Goles"),
        (PARTIDOS_JUGADOS, "Partidos Jugados"),
        (PENALES_ACERTADOS, "Penales acertados"),
        (PENALES_ERRADOS, "Penales errados"),
        (PENALES_ATAJADOS, "Penales Atajados"),
    )

    nombre_estadistca = models.CharField(max_length=50, choices=ESTADISTICA_JUGADOR)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
