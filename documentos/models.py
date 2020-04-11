from django.db import models
from _datetime import datetime

# Create your models here.

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        app_label = "documentos"
        verbose_name_plural = "etiquetas"
    

class Emisor(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
    
    class Meta:
        app_label = "documentos"
        verbose_name_plural = "emisores"
    

class DocumentoOficial(models.Model):
    tema = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=datetime(2020,1,1))
    descripcion = models.TextField(default="", blank=True)
    tipo_de_publicacion = models.ForeignKey(Etiqueta, on_delete=models.PROTECT, null=True)
    emisor = models.ForeignKey(Emisor, on_delete=models.PROTECT, null=True)
    archivo = models.FileField(upload_to='uploads/')
    
    def __str__(self):
        return self.tema
    
    
    class Meta:
        app_label = "documentos"
        verbose_name_plural = "documentos oficiales"
    
