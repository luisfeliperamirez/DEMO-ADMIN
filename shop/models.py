from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_estreno = models.DateField()
    duracion = models.PositiveIntegerField()
    genero = models.CharField(max_length=100)
    director = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo