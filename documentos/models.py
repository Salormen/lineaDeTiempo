from django.db import models
from _datetime import datetime

# Create your models here.

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre


class Hito(models.Model):
    descripcion_corta = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=datetime(2020,1,1))
    descripcion_larga = models.TextField(default="", blank=True)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.descripcion_corta