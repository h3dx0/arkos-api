from rest_framework import serializers
from recursos.models import Recursos


class RecursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recursos
        fields = ['titulo', 'descripcion', 'archivo', 'link_descarga']
