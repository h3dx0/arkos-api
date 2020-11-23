from django.db import models

# Create your models here.


class SistemaArkos(models.Model):
    descripcion = models.TextField()


class BeneficiosSistema(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    def __str__(self):
        return self.titulo