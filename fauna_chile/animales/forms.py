from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre', 'nombre_cientifico', 'habitat', 'estado_conservacion', 'descripcion', 'imagen_url']