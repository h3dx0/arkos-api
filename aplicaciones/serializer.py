from rest_framework import serializers
from aplicaciones.models import Aplicacion, CategoriasAplicacion, ImagenAplicacion


class ImagenAplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenAplicacion
        fields = '__all__'

class AplicacionSerializer(serializers.ModelSerializer):
    imagenes = ImagenAplicacionSerializer(many=True)
    class Meta:
        model = Aplicacion
        fields = '__all__'
        depth = 1

class CategoriaAplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriasAplicacion
        fields = '__all__'

