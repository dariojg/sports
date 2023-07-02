from django.db import models


class CarrouselImage(models.Model):
    image = models.ImageField(upload_to="carrousel", blank=True, null=True)
    orden = models.IntegerField(default=0)
    titulo_imagen = models.CharField(max_length=30)
    activado = models.BooleanField(default=False)


class FooterLink(models.Model):
    pass


class NavLink(models.Model):
    pass
