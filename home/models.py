from django.db import models


class CarrouselImage(models.Model):
    image = models.ImageField(upload_to="carrousel", blank=True, null=True)
    orden = models.IntegerField(default=0)
    titulo_imagen = models.CharField(max_length=30)
    activado = models.BooleanField(default=False)


class ImagesHome(models.Model):
    FOOTER = "footer"
    HEADER = "feader"
    NAV = "nav"
    TIPOS = (
        (FOOTER, "footer"),
        (HEADER, "header"),
        (NAV, "nav"),
    )
    nombre = models.SlugField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="images_home/", blank=True, null=True)
    type = models.CharField(max_length=50, choices=TIPOS, null=True)
    activado = models.BooleanField(default=False)
    # link = models.URLField()
