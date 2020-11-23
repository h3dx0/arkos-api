from django.db import models

# Create your models here.

# Create your models here.

class CategoriasAplicacion(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre


class Aplicacion(models.Model):
    titulo = models.CharField(max_length=250)
    categoria = models.ForeignKey(CategoriasAplicacion, on_delete=models.CASCADE, related_name='aplicacion')
    descripcion = models.TextField()
    imagen = models.FileField(upload_to='proyectos/')
    def __str__(self):
        return self.titulo



class ImagenAplicacion(models.Model):
    imagen = models.FileField(upload_to='aplicaciones/images/')
    nombre = models.CharField(max_length=50)
    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.CASCADE, related_name='imagenes')
    def __str__(self):
        return self.nombre
