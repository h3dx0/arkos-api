from django.db import models

# Create your models here.


class Recursos(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='recursos/')
