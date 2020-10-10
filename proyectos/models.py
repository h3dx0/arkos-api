from django.db import models


# Create your models here.


class CategoriasProyecto(models.Model):
    nombre = models.CharField(max_length=50)


class Proyecto(models.Model):
    titulo = models.CharField(max_length=250)
    categoria = models.ForeignKey(CategoriasProyecto, on_delete=models.CASCADE, related_name='proyecto')
    descripcion = models.TextField()
    imagen = models.FileField(upload_to='proyectos/')


class ImagenProyecto(models.Model):
    imagen = models.FileField(upload_to='proyecto/images/')
    nombre = models.CharField(max_length=50)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='imagenes')

