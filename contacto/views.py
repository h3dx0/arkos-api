from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from contacto.models import Contacto

# Create your views here.
from contacto.serializer import ContactoSerializer


class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
