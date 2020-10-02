from django.shortcuts import render
from rest_framework import viewsets
from quienes_somos.models import QuienesSomos
# Create your views here.
from quienes_somos.serializer import QuienesSomosSerializer


class QuienesSomosViewSet(viewsets.ModelViewSet):
    queryset = QuienesSomos.objects.all()
    serializer_class = QuienesSomosSerializer
