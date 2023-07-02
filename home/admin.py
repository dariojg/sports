from django.contrib import admin
from .models import CarrouselImage


@admin.register(CarrouselImage)
class CarrouselAdmin(admin.ModelAdmin):
    list_display = ["titulo_imagen", "orden"]
    ordering = ["-orden"]
    list_filter = ("titulo_imagen",)
    search_fields = ("titulo_imagen",)
