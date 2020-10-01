from django.db import models

# Create your models here.


# Create your models here.
class Contacto(models.Model):
    telefono = models.CharField(max_length=250)
    telefono_adicional = models.CharField(max_length=250, null=True)
    email = models.EmailField()
    horario = models.TextField()
    calle = models.CharField(max_length=250)
    numero_exterior = models.CharField(max_length=250)
    municipio = models.CharField(max_length=250)
    estado = models.CharField(max_length=250)
    pais = models.CharField(max_length=250)
    codigo_postal = models.CharField(max_length=250)
