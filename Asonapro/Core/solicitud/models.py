from .choices import ESTADOS_VENEZUELA
from django.db import models
from datetime import datetime
from crum import get_current_user

from django.forms import model_to_dict

from Core.solicitante.models import Solicitante
from Core.solicitud.choices import *
from Core.User.models import *

from django.conf import settings
# Create your models here.
from .choicesV import *


class BaseModel(models.Model):
    user_creation = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_creation', null=True, blank=True)
    date_creation = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update', null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "Basemodel"
        verbose_name_plural = "basemodels"
        db_table = 'user'


class Categorias(BaseModel):
    nombre = models.CharField(
        max_length=25, verbose_name='Nombre', unique=True)
    descipcion = models.CharField(
        max_length=250, null=False, blank=False, verbose_name='Descripcion')

    class Meta:
        verbose_name = "Categorias"
        verbose_name_plural = "Categorias"
        db_table = 'Categoria_Solicitud'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_update = user
            super(Categorias, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return str(self.nombre)


class Solicitudes(models.Model):
    fecha_registro = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(
        Categorias, on_delete=models.CASCADE, verbose_name='Categoria')
    id_solicitante = models.ForeignKey(
        Solicitante, on_delete=models.CASCADE, verbose_name='Solicitante')
    estatus = models.CharField(max_length=9, choices=aprobado_choices,
                               default='ESPERA', null=True, blank=True, verbose_name='Estatus')
    descripcion = models.CharField(
        max_length=250, null=False, blank=False, verbose_name='Descripcion')
    descripcion_motivo = models.CharField(
        max_length=250, null=True, blank=True, verbose_name='Descripcion')

    def toJSON(self):
        item = model_to_dict(self)
        item['fecha_registro'] = self.fecha_registro.strftime('%Y-%m-%d')
        item['categoria'] = self.categoria.toJSON()
        item['id_solicitante'] = self.id_solicitante.toJSON()
        return item

    def __str__(self):
        return '{} {} {}'.format(self.id, self.id_solicitante, self.estatus)


class EncargadoBaseMisiones(models.Model):
    cedula = models.CharField(
        max_length=10, unique=True, verbose_name='Cedula')
    fecha_nacimiento = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name='Fecha de nacimiento')
    nombre = models.CharField(
        max_length=50, null=False, blank=False, verbose_name='Nombres')
    apellido = models.CharField(
        max_length=50, null=False, blank=False, verbose_name='Apellidos')
    edad = models.IntegerField()
    sexo = models.CharField(max_length=10, choices=sexo,
                            default='M', null=False, blank=False, verbose_name='Sexo')
    email = models.EmailField(unique=True)
    telefono = models.CharField(
        max_length=30, null=False, blank=False, verbose_name='Telefono')
    codigo = models.CharField(
        max_length=9, unique=True, blank=False, null=False, verbose_name='Codigo')
    serial = models.CharField(
        max_length=9, unique=True, blank=False, null=False, verbose_name='Serial')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{} / {} {}'.format(self.cedula, self.apellido, self.nombre)

    def toJSON(self):
        item = model_to_dict(self)
        item['full_name'] = self.get_full_name()
        item['full_person'] = '{} / {} / {}'.format(
            self.fecha_nacimiento.strftime('%Y-%m-%d'), self.edad, self.sexo)
        item['full_contact'] = '{} / {}'.format(self.telefono, self.email)
        item['datos_patria'] = '{} / {}'.format(self.codigo, self.serial)
        return item

    class Meta:
        verbose_name = 'Encargado'
        verbose_name_plural = 'Encargados'
        db_table = 'Encargados'
        ordering = ['id']


class BaseGrandesMisiones(models.Model):
    nombre = models.CharField(
        max_length=25, verbose_name='Nombre de la Finca', unique=True)
    responsable = models.ForeignKey(
        EncargadoBaseMisiones, on_delete=models.CASCADE, verbose_name='Encargado o Responsable')
    municipio = models.CharField(max_length=100, choices=municipios,
                                 default='GUANARE', null=False, blank=False, verbose_name='Municipios')
    nombre_p = models.CharField(
        max_length=50, null=False, blank=False, verbose_name='Parroquia')
    nombre_c = models.CharField(
        max_length=50, null=False, blank=False, verbose_name='Comunidad')

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        item['responsable'] = self.responsable.toJSON()
        return item

    class Meta:
        verbose_name = 'Fincas_para_produccion'
        verbose_name_plural = 'Fincas_para_produccion'
        db_table = 'Fincas_para_produccion'
        ordering = ['id']


# INSPECCIONES PREVIAS
class VocacionTierra(models.Model):
    nombre = models.CharField(max_length=100, choices=VocacionTierra.choices)

    def __str__(self):
        return self.nombre


class Material_vivienda(models.Model):
    nombre = models.CharField(max_length=50, choices=MaterialVivienda.choices)

    def __str__(self):
        return self.nombre


class OpcionesElectricidad(models.Model):
    nombre = models.CharField(
        max_length=100, choices=Opcioneselectricidad.choices)

    def __str__(self):
        return self.nombre


class OpcionesTransporte(models.Model):
    nombre = models.CharField(
        max_length=100, choices=OpcionesTransporte.choices)

    def __str__(self):
        return self.nombre


class OpcionesTelefono(models.Model):
    nombre = models.CharField(
        max_length=100, choices=OpcionesTelefonoChoices.choices)

    def __str__(self):
        return self.nombre


class OpcionesGas(models.Model):
    nombre = models.CharField(
        max_length=100, choices=OpcionesGasChoices.choices)

    def __str__(self):
        return self.nombre


class OpcionesAguaBlancas(models.Model):
    nombre = models.CharField(
        max_length=100, choices=OpcionesAguasBlancasChoices.choices)

    def __str__(self):
        return self.nombre


class OpcionesAguasServidas(models.Model):
    nombre = models.CharField(
        max_length=100, choices=OpcionesAguasServidasChoices.choices)

    def __str__(self):
        return self.nombre


class OpcionDrenaje(models.Model):
    nombre = models.CharField(
        max_length=20, choices=OpcionesDrenajeChoices.choices, unique=True)

    def __str__(self):
        return self.nombre


class FuenteAgua(models.Model):
    nombre = models.CharField(max_length=20, choices=FUENTES_AGUA, unique=True)

    def __str__(self):
        return self.nombre


class SistemaRiego(models.Model):
    nombre = models.CharField(
        max_length=100,  choices=SistemaRiegoChoices.choices)

    def __str__(self):
        return self.nombre


# INSPECCION DE LA FINCA
class Inspeccion(models.Model):
    Sembrador_user = models.ForeignKey(
        Sembradores, on_delete=models.CASCADE, null=True)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, null=True)
    nombre_unidad = models.CharField(max_length=50)
    direccion_unidad = models.CharField(max_length=100)
    como_llegar = models.TextField(max_length=100)
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    parroquia = models.CharField(max_length=50)
    vive_en_unidad = models.BooleanField(default=False)
    frecuencia_visita = models.CharField(
        max_length=10,
        choices=FrecuenciaVisita.choices,
        default=FrecuenciaVisita.DIARIO,
        blank=True,
        null=True
    )
    tenencia_de_tierra = models.CharField(
        max_length=50, choices=TenenciaDeTierra.choices, blank=True)
    vocacion_tierra = models.ManyToManyField(VocacionTierra, blank=True)
    vivienda = models.BooleanField(default=False)
    material_vivienda = models.ManyToManyField(Material_vivienda)

    electricidad = models.CharField(
        max_length=3,
        choices=Electricidad.choices,
        default=Electricidad.SI
    )
    opciones_electricidad = models.ManyToManyField(
        OpcionesElectricidad,  blank=True)

    transporte_insumo = models.CharField(
        max_length=3,
        choices=TransporteInsumos.choices,
        default=TransporteInsumos.SI
    )
    opciones_transporte = models.ManyToManyField(
        OpcionesTransporte, blank=True)

    telefono = models.CharField(
        max_length=3,
        choices=TelefonoChoices.choices,
        default=TelefonoChoices.SI,
    )
    opciones_telefono = models.ManyToManyField(OpcionesTelefono, blank=True)

    gas = models.CharField(
        max_length=3,
        choices=GasChoices.choices,
        default=GasChoices.SI
    )
    opciones_gas = models.ManyToManyField(OpcionesGas, blank=True)

    aguas_blancas = models.CharField(
        max_length=3,
        choices=AguasBlancasChoices.choices,
        default=AguasBlancasChoices.SI
    )
    opciones_aguas_blancas = models.ManyToManyField(
        OpcionesAguaBlancas, blank=True)

    aguas_servidas = models.CharField(
        max_length=3,
        choices=AguasBlancasChoices.choices,
        default=AguasBlancasChoices.SI
    )

    opciones_aguas_servidas = models.ManyToManyField(
        OpcionesAguasServidas, blank=True)

    superficie_total_up = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Superficie Total de la UP (ha)"
    )
    superficie_aprovechable_up = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Superficie Aprovechable de la UP (ha)"
    )
    superficie_gps = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Superficie Medida con GPS (ha)"

    )

    fuentes_agua = models.ManyToManyField(FuenteAgua, blank=True)

    drenaje_opciones = models.ManyToManyField(OpcionDrenaje, blank=True)

    condiciones_drenaje = models.CharField(
        max_length=20,
        choices=CondicionesDrenajeChoices.choices,
        blank=True,
        null=True
    )

    sistema_riego = models.ManyToManyField(SistemaRiego, blank=True)

    condiciones_sistema_riego = models.CharField(
        max_length=20,
        choices=CondicionesSistemaRiegoChoices.choices,
        blank=True,
        null=True
    )

    superficie_externa = models.CharField(
        max_length=20,
        choices=SuperficieExternaChoices.choices,
        blank=True,
        null=True
    )
    superficie_interna = models.CharField(
        max_length=20,
        choices=SuperficieInternaChoices.choices,
        blank=True,
        null=True
    )

    def toJSON(self):
        item = model_to_dict(self, exclude=[
                             'id', 'Sembrador_user', 'tecnico', 'electricidad', 'transporte_insumo', 'telefono', 'gas', 'aguas_blancas', 'aguas_servidas', 'superficie_total_up', 'superficie_aprovechable_up', 'superficie_gps', 'condiciones_drenaje', 'condiciones_sistema_riego', 'superficie_externa', 'superficie_interna', 'vocacion_tierra', 'material_vivienda', 'opciones_electricidad', 'opciones_transporte', 'opciones_telefono', 'opciones_gas', 'opciones_aguas_blancas', 'opciones_aguas_servidas', 'fuentes_agua', 'drenaje_opciones', 'sistema_riego'])

        item['full_name'] = self.Sembrador_user.get_full_name()
        item['full_name_tecnico'] = self.tecnico.get_full_name()

        return item

    def __str__(self):
        return '{} | {} | {}'.format(self.Sembrador_user.get_full_name(), self.tecnico.get_full_name(), self.nombre_unidad)

    class Meta:
        db_table = 'Inspecciones'

# se callo el puente


class Seguimiento(models.Model):
    seguimiento_id = models.AutoField(primary_key=True)
    Sembrador_user = models.ForeignKey(
        Sembradores, on_delete=models.CASCADE, null=True, verbose_name="Sembrador User")
    nombre_persona_atendio = models.CharField(
        max_length=50, null=False, verbose_name="Nombre Persona Atendio")
    cedula = models.CharField(max_length=9, blank=True,
                              null=False, verbose_name="Cedula")
    tlf = models.CharField(max_length=11, blank=True,
                           null=False, verbose_name="Telefono")
    fecha_visita = models.DateField(
        auto_now=False, verbose_name="Fecha de Visita")
    fecha_proxima_visita = models.DateField(
        auto_now=False, verbose_name="Fecha Proxima de Visita")

    motivo_visita = models.CharField(
        max_length=10, choices=MOTIVO_CHOICES, null=False, verbose_name="Motivo de Visita")
    lote1 = models.CharField(max_length=5, blank=True,
                             null=True, verbose_name="Lote 1")
    lote2 = models.CharField(max_length=5, blank=True,
                             null=True, verbose_name="Lote 2")
    lote3 = models.CharField(max_length=5, blank=True,
                             null=True, verbose_name="Lote 3")
    lote4 = models.CharField(max_length=5, blank=True,
                             null=True, verbose_name="Lote 4")

    edad_cultivo = models.CharField(
        max_length=9, verbose_name="Edad del Cultivo")
    superficie_up = models.FloatField(verbose_name="Superficie Up")
    superficie_preparada = models.FloatField(
        max_length=10, blank=True, verbose_name="Superficie Preparada")
    superficie_sembrada = models.FloatField(
        max_length=10, blank=True, verbose_name="Superficie Sembrada")
    rubro_sembrado = models.CharField(
        max_length=20, verbose_name="Rubro Sembrado")
    semilla_variedad = models.CharField(
        max_length=20, verbose_name="Semilla Variedad")
    realizar_recomendacion = models.CharField(
        max_length=2, choices=RECOMENDACION, verbose_name="Realizar Recomendacion")
    fecha_estimada_cosecha = models.DateField(
        auto_now=False, verbose_name="Fecha Estimada de Cosecha")

    superficie_por_consechar = models.FloatField(
        max_length=10, blank=True, verbose_name="Superficie Por Consechar")
    superficie_cosechada = models.FloatField(
        max_length=10, blank=True, verbose_name="Superficie Cosechada")
    superficie_perdida = models.FloatField(
        max_length=10, blank=True, verbose_name="Superficie Perdida")
    superficie_efectiva = models.FloatField(
        max_length=10, blank=True, verbose_name="Superficie Efectiva")

    estimacion_del_redimiento = models.CharField(
        max_length=20, verbose_name="Estimacion del Rendimiento")
    redimiento = models.CharField(max_length=20, verbose_name="Rendimiento")
    redimiento_total = models.CharField(
        max_length=20, verbose_name="Rendimiento Total")
    dar_continuidad = models.CharField(
        max_length=20, choices=RECOMENDACION, verbose_name="Dar Continuidad")
    descripcion = models.TextField(max_length=200, verbose_name="Descripcion")
    coordenadas_norte = models.CharField(
        max_length=10, verbose_name="Coordenadas Norte")
    coordenadas_sur = models.CharField(
        max_length=10, verbose_name="Coordenadas Sur")
    tecnico = models.ForeignKey(
        Tecnico, on_delete=models.CASCADE, related_name='seguimientos_tecnico', verbose_name="Tecnico")

    def toJSON(self, exclude=['seguimiento_id','fecha_visita', 'fecha_proxima_visita', 'fecha_estimada_cosecha']):
        item = model_to_dict(self)

        item['full_name'] = self.Sembrador_user.get_full_name()

        item['fecha_visita'] = self.fecha_visita.strftime('%Y-%m-%d')
        item['fecha_proxima_visita'] = self.fecha_visita.strftime('%Y-%m-%d')
        item['fecha_estimada_cosecha'] = self.fecha_visita.strftime('%Y-%m-%d')

        item['tecnico_name'] = '{} {}'.format(
            self.tecnico.first_name, self.tecnico.last_name)
        

        return item

    class Meta:
        verbose_name = "Seguimiento"
        verbose_name_plural = "Seguimientos"
