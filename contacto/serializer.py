from rest_framework import serializers
from contacto.models import Contacto


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ['telefono', 'telefono_adicional', 'email','horario', 'calle', 'numero_exterior', 'municipio',
                  'estado', 'pais', 'codigo_postal']
