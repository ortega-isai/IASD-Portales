from django.db import models
from django.urls import reverse


class Oracion(models.Model):
    nombre = models.CharField(max_length=254, verbose_name='Nombre')
    fecha_hora = models.DateTimeField(
        verbose_name='Fecha y Hora de la oración', unique=True)
    motivo = models.TextField(
        verbose_name='Por quien o por que de la oración')
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['fecha_hora']
        verbose_name = "Oracion"
        verbose_name_plural = "Oraciones"

    def __str__(self):
        return '{} - {}'.format(self.id, self.nombre)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this empresa."""
        return reverse('oracion_detail', args=[int(self.pk)])

    def get_absolute_url_udpate(self):
        """Returns the url to access a detail record for this cliente."""
        return reverse('oracion_update', args=[int(self.pk)])
