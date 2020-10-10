from django.shortcuts import render
from rest_framework import viewsets
from sistema_arkos.models import  BeneficiosSistema, SistemaArkos
from sistema_arkos.serializer import BeneficiosArkosSerializer, SistemaArkosSerializer
# Create your views here.


class SistemaViewSet(viewsets.ModelViewSet):
    queryset = SistemaArkos.objects.all()
    serializer_class = SistemaArkosSerializer

class BeneficiosViewSet(viewsets.ModelViewSet):
    queryset = BeneficiosSistema.objects.all()
    serializer_class = BeneficiosArkosSerializer