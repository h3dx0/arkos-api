from rest_framework import serializers
from inicio.models import Inicio, CategoriasGaleria, ImagenGaleriaInicio, ComentarioClientesInicio


class InicioSerializer(serializers.ModelSerializer):
    categorias = serializers.ModelField
    class Meta:
        model = Inicio
        fields = ['imagen_slider', 'nombre_primer_servicio', 'descripcion_primer_servicio', 'nombre_segundo_servicio',
                  'descripcion_segundo_servicio','nombre_tercer_servicio','descripcion_tercer_servicio']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriasGaleria
        fields = ['nombre']

class ImagenGaleriaInicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenGaleriaInicio
        fields = ['nombre','imagen','categoria']
        depth = 1

class ComentarioClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentarioClientesInicio
        fields = ['nombre','imagen','comentario']
