from django.contrib import admin
from .models import Placa, Video


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1


@admin.register(Placa)
class PlacaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo', 'ubicacion_fisica', 'fecha_creacion']
    list_filter = ['tipo']
    search_fields = ['nombre', 'descripcion']
    inlines = [VideoInline]
