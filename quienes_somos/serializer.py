from rest_framework import serializers
from quienes_somos.models import QuienesSomos


class QuienesSomosSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuienesSomos
        fields = ['historia', 'mision', 'vision']
