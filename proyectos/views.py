from django.shortcuts import render
from rest_framework import viewsets
from proyectos.models import  Proyecto
# Create your views here.
from proyectos.serializer import ProyectoSerializer


class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
