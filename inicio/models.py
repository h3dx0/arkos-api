from django.db import models


# Create your models here.
class Inicio(models.Model):
    imagen_slider = models.FileField(upload_to='inicio/images/')

    nombre_primer_servicio = models.CharField(max_length=50)
    descripcion_primer_servicio = models.TextField(max_length=250)
    nombre_segundo_servicio = models.CharField(max_length=50)
    descripcion_segundo_servicio = models.TextField(max_length=250)
    nombre_tercer_servicio = models.CharField(max_length=50)
    descripcion_tercer_servicio = models.TextField(max_length=250)


class CategoriasGaleria(models.Model):
    nombre = models.CharField(max_length=50)


class ImagenGaleriaInicio(models.Model):
    imagen = models.FileField(upload_to='inicio/images/proyectos/')
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriasGaleria, on_delete=models.CASCADE, related_name='imagenes')
