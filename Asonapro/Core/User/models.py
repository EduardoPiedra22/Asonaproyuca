from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone
from django.forms import model_to_dict
from crum import get_current_request
from Config.settings import MEDIA_URL, STATIC_URL
from Core.User.choice import *


class User(AbstractUser):
    imagen = models.ImageField(
        upload_to='users1/%Y/%m/%d', null=True, blank=True)
    token = models.UUIDField(
        unique=False, null=True, editable=False, blank=True)

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/user.png')

    def toJSON(self):
        item = model_to_dict(
            self, exclude=['password', 'user_permissions', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['imagen'] = self.get_image()
        item['full_name'] = self.get_full_name()
        item['groups'] = [{'id': g.id, 'name': g.name}
                          for g in self.groups.all()]
        return item

    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass

    def __str__(self):
        return '{}'.format(self.username)

    class Meta:
        db_table = 'Usuarios'


class Sembradores(User):
    cedula = models.CharField(max_length=10, null=True,
                              blank=True, verbose_name="Cédula")
    cedula_agraria = models.CharField(
        max_length=10, null=True, blank=True, verbose_name="Cédula Agraria")
    codigo_asonaproyuca = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Código Asonaproyuca")
    fecha_registro = models.DateTimeField(default=timezone.now)
    fecha_actualizacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Actualización")
    telefono_personal = models.CharField(
        max_length=15, null=True, blank=True, verbose_name="Teléfono Personal")
    telefono_casa = models.CharField(
        max_length=15, null=True, blank=True, verbose_name="Teléfono de Casa")
    direccion = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Dirección")
    fecha_nacimiento = models.DateField(
        null=True, blank=True, verbose_name="Fecha de Nacimiento")
    edad = models.IntegerField(null=True, blank=True, verbose_name="Edad")
    estado_civil = models.CharField(
        max_length=30, choices=ESTADO_CIVIL_CHOICES, verbose_name="Estado Civil")
    profesion_ocupacion = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Profesión u Ocupación")
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES,
                            null=True, blank=True, verbose_name="Sexo")
    logue_complete = models.BooleanField(
        default=False, verbose_name="Registro Completo")

    # NUEVOS CAMPOS
    estado = models.CharField(max_length=50, null=True,
                              blank=True, verbose_name="Estado")
    municipio = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Municipio")
    parroquia = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Parroquia")

    nombre_unidad = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Nombre de la Unidad")

    # Datos del Conyuge
    conyuge_nombre = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Nombre del Cónyuge")
    conyuge_apellido = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Apellido del Cónyuge")
    conyuge_cedula = models.CharField(
        max_length=10, unique=True, null=True, blank=True, verbose_name="Cédula del Cónyuge")
    conyuge_edad = models.IntegerField(
        null=True, blank=True, verbose_name="Edad del Cónyuge")
    conyuge_sexo = models.CharField(
        max_length=10, choices=SEXO_CHOICES, null=True, blank=True, verbose_name="Sexo del Cónyuge")
    conyuge_telefono_fijo = models.CharField(
        max_length=15, null=True, blank=True, verbose_name="Teléfono Fijo del Cónyuge")
    conyuge_telefono_celular = models.CharField(
        max_length=15, null=True, blank=True, verbose_name="Teléfono Celular del Cónyuge")

    # Datos de la dirección de Habitacion
    direccion_habitacion_estado = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Estado de la Dirección de Habitación")
    direccion_habitacion_municipio = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Municipio de la Dirección de Habitación")
    direccion_habitacion_parroquia = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Parroquia de la Dirección de Habitación")
    direccion_habitacion_caserio = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Caserío de la Dirección de Habitación")
    direccion_habitacion_sector = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Sector de la Dirección de Habitación")
    direccion_habitacion_ciudad_cercana = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Ciudad Cercana de la Dirección de Habitación")
    direccion_habitacion_punto_referencia = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Punto de Referencia de la Dirección de Habitación")
    direccion_habitacion_direccion = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Dirección de Habitación")

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/user.png')

    def toJSON(self):
        item = model_to_dict(
            self, exclude=['fecha_nacimiento', 'edad', 'fecha_nacimiento', 'direccion', 'telefono_casa', 'telefono_personal', 'fecha_actualizacion', 'estado_civil', 'logue_complete', 'password', 'user_permissions', 'last_login',
                           'is_superuser', 'is_staff', 'is_active', 'token', 'date_joined', 'imagen', 'groups', 'user_ptr', 'sexo', 'profesion_ocupacion'])
        item['full_name'] = self.get_full_name()

        return item

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = "Sembrador"
        verbose_name_plural = "Sembradores"


class Tecnico(User):
    cedula = models.CharField(max_length=20, null=True, blank=True)
    estado = models.CharField(max_length=100, null=True)
    oficina = models.CharField(max_length=100, null=True, blank=True)
    profesion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    logue_complete = models.BooleanField(default=False)

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/user.png')

    def toJSON(self):
        item = model_to_dict(
            self, exclude=['password', 'user_permissions', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['imagen'] = self.get_image()
        item['full_name'] = '{} {}'.format(
            self.first_name, self.last_name)
        item['groups'] = [{'id': g.id, 'name': g.name}
                          for g in self.groups.all()]
        item['full_contact'] = '{} / {}'.format(
            self.telefono, self.email)
        item['cedula'] = self.cedula
        return item

    def __str__(self):
        return '{}'.format(self.first_name)

    class Meta:
        db_table = 'Tecnicos'
