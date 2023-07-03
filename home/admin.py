from django.contrib import admin
from .models import CarrouselImage, ImagesHome


@admin.register(CarrouselImage)
class CarrouselAdmin(admin.ModelAdmin):
    list_display = ["titulo_imagen", "orden", "activado"]
    ordering = ["-orden"]
    list_filter = ("titulo_imagen", "activado",)
    search_fields = ("titulo_imagen",)


@admin.register(ImagesHome)
class ImagesHome(admin.ModelAdmin):
    list_display = [
        "nombre",
        "type",
        "activado",
    ]
    list_filter = (
        "nombre",
        "type",
        "activado",
    )
    search_fields = (
        "nombre",
        "type",
    )
