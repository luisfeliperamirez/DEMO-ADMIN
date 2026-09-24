from django.contrib import admin
from .models import Pelicula

class PeliculasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_estreno', 'duracion', 'genero', 'director')
    search_fields = ('titulo', 'genero', 'director')
    list_filter = ('fecha_estreno', 'genero')

admin.site.register(Pelicula, PeliculasAdmin)