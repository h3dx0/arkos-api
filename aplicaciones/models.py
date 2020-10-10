from django.db import models

# Create your models here.

# Create your models here.

class CategoriasAplicacion(models.Model):
    nombre = models.CharField(max_length=50)


class Aplicacion(models.Model):
    titulo = models.CharField(max_length=250)
    categoria = models.ForeignKey(CategoriasAplicacion, on_delete=models.CASCADE, related_name='aplicacion')
    descripcion = models.TextField()
    imagen = models.FileField(upload_to='proyectos/')



class ImagenAplicacion(models.Model):
    imagen = models.FileField(upload_to='aplicaciones/images/')
    nombre = models.CharField(max_length=50)
    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.CASCADE, related_name='imagenes')

