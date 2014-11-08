from django.db import models

from asociaciones.models import Asociacion

class Linea(models.Model):
    nombre = models.CharField(max_length='10')

    asociacion = models.ForeignKey(Asociacion, null=True, blank=True)
    def __unicode__(self):
        return self.nombre
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Lineas'
        permissions = (
            ('detail_linea', 'Detalle De Linea'),
            ('rutas_linea', 'Rutas de Linea'),
        )

class Posicion(models.Model):
    latitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    inicio = models.BooleanField(default=False)
    fin = models.BooleanField(default=False)
    subida = models.BooleanField(default=False)
    bajada = models.BooleanField(default=False)
    linea = models.ForeignKey(Linea, null=True, blank=True)
    def __unicode__(self):
        return self.linea.nombre

class Zona(models.Model):
    nombre = models.CharField(max_length='20', unique=True)
    def __unicode__(self):
        return self.nombre
    class Meta:
        ordering = ['nombre']

class Calle(models.Model):
    nombre = models.CharField(max_length='30', verbose_name=u'Nombre de Calle/Avenida')
    zona = models.ForeignKey(Zona)
    def __unicode__(self):
        return self.nombre

class Posicion_Calle(models.Model):
    posicion = models.ForeignKey(Posicion)
    calle = models.ForeignKey(Calle)
    def __unicode__(self):
        return self.calle.nombre