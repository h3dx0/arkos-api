from django.shortcuts import render

from recursos.models import Recursos
from recursos.serializer import RecursosSerializer
from rest_framework import viewsets

# Create your views here.


class RecursosViewSet(viewsets.ModelViewSet):
    queryset = Recursos.objects.all()
    serializer_class = RecursosSerializer
