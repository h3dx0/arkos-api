from django.http.response import Http404
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from proyectos.models import  Proyecto, CategoriasProyecto
# Create your views here.
from proyectos.serializer import ProyectoSerializer, CategoriaProyectoSerializer


class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class CategoriaProyectoViewSet(viewsets.ModelViewSet):
    queryset = CategoriasProyecto.objects.all()
    serializer_class = CategoriaProyectoSerializer

class ProyectoDetalle(APIView):

    def get_object(self,pk):
        try:
            return Proyecto.objects.get(pk=pk)
        except Proyecto.DoesNotExist:
            raise Http404

    def get(self,request, pk, format=None):
        aplicacion = self.get_object(pk)
        serializer = ProyectoSerializer(aplicacion)
        return Response(serializer.data)