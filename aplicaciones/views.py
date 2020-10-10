from django.http.response import Http404
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from aplicaciones.models import Aplicacion, CategoriasAplicacion
from aplicaciones.serializer import AplicacionSerializer, CategoriaAplicacionSerializer


class AplicacionViewSet(viewsets.ModelViewSet):
    queryset = Aplicacion.objects.all()
    serializer_class = AplicacionSerializer

class CategoriaAplicacionViewSet(viewsets.ModelViewSet):
    queryset = CategoriasAplicacion.objects.all()
    serializer_class = CategoriaAplicacionSerializer

class AplicacionDetalle(APIView):

    def get_object(self,pk):
        try:
            return Aplicacion.objects.get(pk=pk)
        except Aplicacion.DoesNotExist:
            raise Http404

    def get(self,request, pk, format=None):
        aplicacion = self.get_object(pk)
        serializer = AplicacionSerializer(aplicacion)
        return Response(serializer.data)