from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_cientifico = models.CharField(max_length=150)
    habitat = models.CharField(max_length=200)
    estado_conservacion = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.nombre