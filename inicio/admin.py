from django.contrib import admin

# Register your models here.
from inicio.models import Inicio, CategoriasGaleria, ImagenGaleriaInicio, ComentarioClientesInicio

admin.site.register(Inicio)
admin.site.register(CategoriasGaleria)
admin.site.register(ImagenGaleriaInicio)
admin.site.register(ComentarioClientesInicio)