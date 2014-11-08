from django.db import models
from django.contrib.auth.models import User
from geoposition.fields import GeopositionField

class Asociacion(models.Model):
    nombre = models.CharField(max_length='30')
    direccion = models.CharField(max_length='100')
    telefono = models.CharField(max_length='10')
    email = models.EmailField(verbose_name='Correo Electronico', unique=True)
    position = GeopositionField()
    usuario = models.OneToOneField(User, null=True, blank=True)
    def __unicode__(self):
        return self.nombre
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Asociaciones'
        permissions = (
            ('detail_asociacion', 'Detalle de Asociacion'),
            ('report_asociacion', 'Reporte de Asociacion'),
            ('mi_asociacion', 'Permisos Asociacion '),
        )
