from django.db import models


class Partido(models.Model):
    club_local = models.CharField(max_length=100)
    club_visitante = models.CharField(max_length=100)
    imagen_escudo = models.ImageField(upload_to="escudos/", blank=True, null=True)
    fecha_partido = models.DateTimeField()
    estadio = models.CharField(max_length=50, default="")
    activado = models.BooleanField(default=False)

    def __str__(self):
        return "{} vs {}".format(self.club_local, self.club_visitante)


class Formacion(models.Model):
    posicion = models.CharField(max_length=30)
    nombre_jugador = models.CharField(max_length=100)  # TODO ver si conviene FK a jugadores
    club = models.CharField(max_length=30)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.nombre_jugador, self.posicion)
