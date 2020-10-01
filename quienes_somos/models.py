from django.db import models

# Create your models here.


class QuienesSomos(models.Model):
    historia = models.TextField()
    mision = models.TextField(null=True)
    vision = models.TextField(null=True)
