from django.contrib import admin
from .models import Componente


@admin.register(Componente)
class ComponenteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'valor', 'categoria', 'cantidad', 'ubicacion']
    list_filter = ['categoria']
    search_fields = ['nombre', 'valor', 'ubicacion']
