from django.db import models
from artistas.models import Artista

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    anio_lanzamiento = models.IntegerField()
    genero = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    portada = models.ImageField(upload_to='portadas/')

    def __str__(self):
        return self.titulo