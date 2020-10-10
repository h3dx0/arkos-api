from django.contrib import admin

# Register your models here.
from aplicaciones.models import Aplicacion, CategoriasAplicacion, ImagenAplicacion

class ImagenAdmin(admin.TabularInline):
    model = ImagenAplicacion

class AplicacionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria','descripcion']
    inlines = [
        ImagenAdmin,
    ]
admin.site.register(Aplicacion, AplicacionAdmin)
admin.site.register(CategoriasAplicacion)
admin.site.register(ImagenAplicacion)