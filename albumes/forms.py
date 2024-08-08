from django import forms
from .models import Album
from django.forms.widgets import ClearableFileInput

class CustomClearableFileInput(ClearableFileInput):
    initial_text = 'Actual'
    input_text = 'Cambiar'
    clear_checkbox_label = 'Eliminar'

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'anio_lanzamiento', 'genero', 'artista', 'portada']
        labels = {
            'titulo': 'Título del Álbum',
            'artista': 'Artista',
            'anio_lanzamiento': 'Año de Lanzamiento',
            'genero': 'Género',
            'portada': 'Portada',
        }
        widgets = {
            'portada': CustomClearableFileInput,
        }