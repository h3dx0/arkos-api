from django.contrib import admin

# Register your models here.
from proyectos.models import Proyecto, ImagenProyecto, CategoriasProyecto


class ImagenAdmin(admin.TabularInline):
    model = ImagenProyecto

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria','descripcion', 'imagen']
    inlines = [
        ImagenAdmin,
    ]
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(CategoriasProyecto)