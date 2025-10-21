from django.contrib import admin
from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nombre_cientifico', 'estado_conservacion']
    search_fields = ['nombre', 'habitat']
    list_filter = ['estado_conservacion']