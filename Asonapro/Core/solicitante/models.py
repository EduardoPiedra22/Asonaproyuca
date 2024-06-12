from datetime import datetime
from django.db import models
from django.forms import model_to_dict
from Config.settings import MEDIA_URL, STATIC_URL
from Core.models import BaseModel
from Core.solicitud.choices import *

from crum import get_current_user
# lsp lsp-pyright
# Create your models here.


class Solicitante(BaseModel):
    """
    Description: Model Solicitantes
    """
    tipo_documento = models.CharField(max_length=45, choices=tipo_documento,
                                      default='V', null=False, blank=False, verbose_name='Tipo de documento')

    fecha_registro = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    fecha_actulizacion = models.DateTimeField(
        auto_now=True, null=True, blank=True)
    cedula = models.CharField(
        max_length=10, unique=True, verbose_name='Cedula')
    nombre = models.CharField(max_length=25, verbose_name='Nombres')
    apellido = models.CharField(max_length=25, verbose_name='Apellido')
    telefono = models.CharField(max_length=30, verbose_name='Telefono')
    correo_electronico = models.EmailField()
    direccion = models.CharField(
        max_length=150, null=True, blank=True, verbose_name='Dirección')
    fecha_nacimiento = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name='Fecha de nacimiento')
    edad = models.IntegerField()
    sexo = models.CharField(max_length=10, choices=sexo,
                            default='M', null=False, blank=False, verbose_name='Sexo')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{} {} / {}'.format(self.nombre, self.apellido, self.cedula)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_update = user
            super(Solicitante, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        item['fecha_registro'] = self.fecha_registro.strftime(
            '%Y-%m-%d %H:%M:%S')
        item['fecha_actulizacion'] = self.fecha_actulizacion.strftime(
            '%Y-%m-%d %H:%M:%S')
        item['full_name'] = self.get_full_name()
        item['full_contact'] = '{} / {}'.format(
            self.telefono, self.correo_electronico)
        item['full_person'] = '{} / {} / {}'.format(
            self.fecha_nacimiento.strftime('%Y-%m-%d'), self.edad, self.sexo)
        return item

    class Meta:
        verbose_name = 'Solicitante'
        verbose_name_plural = 'Solicitantes'
        db_table = 'Solicitantes'
        ordering = ['id']
