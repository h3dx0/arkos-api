from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import permissions
from contacto.models import Contacto

# Create your views here.
from contacto.serializer import ContactoSerializer


class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

@csrf_exempt
def send_email(request):

    return JsonResponse({"aa": "ok"})