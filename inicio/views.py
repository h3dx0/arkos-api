from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from inicio.models import Inicio, CategoriasGaleria, ImagenGaleriaInicio, ComentarioClientesInicio
from inicio.serializer import InicioSerializer, CategoriaSerializer, ImagenGaleriaInicioSerializer, \
    ComentarioClienteSerializer


class InicioViewSet(viewsets.ModelViewSet):
    queryset = Inicio.objects.all()
    serializer_class = InicioSerializer

class CategoriaGaleriaViewSet(viewsets.ModelViewSet):
    queryset = CategoriasGaleria.objects.all().order_by('-id')
    serializer_class = CategoriaSerializer

class ImagenGaleriaViewSet(viewsets.ModelViewSet):
    queryset = ImagenGaleriaInicio.objects.all()
    serializer_class = ImagenGaleriaInicioSerializer

class ComentarioClienteViewSet(viewsets.ModelViewSet):
    queryset = ComentarioClientesInicio.objects.all()
    serializer_class = ComentarioClienteSerializer