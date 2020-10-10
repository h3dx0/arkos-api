from rest_framework import serializers
from proyectos.models import Proyecto, ImagenProyecto, CategoriasProyecto


class ImagenProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenProyecto
        fields = '__all__'


class ProyectoSerializer(serializers.ModelSerializer):
    imagenes = ImagenProyectoSerializer(many=True)
    class Meta:
        model = Proyecto
        fields = ['titulo', 'categoria', 'descripcion', 'imagen','imagenes']

class CategoriaProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriasProyecto
        fields = '__all__'

