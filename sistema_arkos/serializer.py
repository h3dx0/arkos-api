from rest_framework import serializers
from sistema_arkos.models import SistemaArkos, BeneficiosSistema


class SistemaArkosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SistemaArkos
        fields = ['descripcion']

class BeneficiosArkosSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeneficiosSistema
        fields = ['titulo','descripcion']
