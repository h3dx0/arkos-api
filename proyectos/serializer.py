from rest_framework import serializers
from proyectos.models import Proyecto


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'categoria', 'descripcion', 'imagen']
