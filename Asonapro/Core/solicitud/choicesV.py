# choices.py
from django.db import models
from django.utils.translation import gettext as _

# Definir las opciones para "Frecuencia de Visita"


class FrecuenciaVisita(models.TextChoices):
    DIARIO = 'diario', _('Diario')
    SEMANAL = 'semanal', _('Semanal')
    MENSUAL = 'mensual', _('Mensual')
    ANUAL = 'anual', _('Anual')


# Tenencia de Tierra
class TenenciaDeTierra(models.TextChoices):
    INIT = 'init', _('Init')
    BLANDIA = 'blandia', _('Blandia')
    PROPIA = 'propia', _('Propia')
    EJIDO = 'ejido', _('Ejido')
    ZONA_PROTEGIDA = 'zona_protegida', _('Zona Protegida PERMITIDA')
    OTROS = 'otros', _('Otros')


# Vocacion de la tierra
class VocacionTierra(models.TextChoices):
    AGRICOLA = 'agricola', _('Agrícola')
    PECUARIO = 'pecuario', _('Pecuario')
    FORESTAL = 'forestal', _('Forestal')
    ACUICOLA = 'acuicola', _('Acuícola')
    MINERAL = 'mineria', _('Minería')
    TURISMO = 'turismo', _('Turismo')
    OTROS = 'otros', _('Otros')


# Servicios basicos existentes en la unidad de produccion
class Vivienda(models.TextChoices):
    SI = 'si', _('Sí')
    NO = 'no', _('No')


# Material con el que esta estructurada la Finca
class MaterialVivienda(models.TextChoices):
    BAHAREQUE = 'bahareque', _('Bahareque')
    BLOQUE = 'bloque', _('Bloque')
    ZINC = 'zinc', _('Zinc')
    OTROS = 'otros', _('Otros')


# Cuenta con servicio Electrico
class Electricidad(models.TextChoices):
    SI = 'si', _('Si')
    NO = 'no', _('No')


# Definir las opciones para "Opciones de Electricidad"
class OpcionesElectricidad(models.TextChoices):
    PLANTA = 'planta', _('Planta Eléctrica')
    GENERADOR = 'generador', _('Generador Eléctrico')
    TENIDO = 'tendido', _('Tendido Eléctrico')


# Transporte de Isumos
class TransporteInsumos(models.TextChoices):
    SI = 'si', _('Si')
    NO = 'no', _('No')


# Definir las opciones para "Opciones de Transporte de Insumo"
class OpcionesTransporte(models.TextChoices):
    PICKUP = 'pickup', _('Pick Up')
    CAMION350 = '350', _('350')
    CAMION750 = '750', _('750')
    GANDOLA = 'gandola', _('Gandola')
    OTROS = 'otros', _('Otros')


class TelefonoChoices(models.TextChoices):
    SI = 'si', _('Sí')
    NO = 'no', _('No')


class OpcionesTelefonoChoices(models.TextChoices):
    FIJO = 'fijo', _('Fijo')
    MOVIL = 'movil', _('Móvil')
    OTROS = 'otros', _('Otros')


class GasChoices(models.TextChoices):
    SI = 'si', _('Sí')
    NO = 'no', _('No')


class OpcionesGasChoices(models.TextChoices):
    DIRECTO = 'directo', _('Directo')
    BOMBONA = 'bombona', _('Bombona')
    OTROS = 'otros', _('Otros')


class AguasBlancasChoices(models.TextChoices):
    SI = 'si', _('Sí')
    NO = 'no', _('No')


class OpcionesAguasBlancasChoices(models.TextChoices):
    POZO = 'pozo', _('Pozo')
    JAGUEY = 'jaguey', _('Jagüey')
    ACUEDUCTO = 'acueducto', _('Acueducto')
    CISTERNA = 'cisterna', _('Cisterna')
    OTROS = 'otros', _('Otros')


class OpcionesDrenajeChoices(models.TextChoices):
    CANALES = 'canales', _('Canales')
    SUPERFICIAL = 'superficial', _('Superficial')
    NATURAL = 'natural', _('Natural')
    ZANJA = 'zanja', _('Zanja')


class CondicionesDrenajeChoices(models.TextChoices):
    BUENO = 'bueno', _('Bueno')
    REGULAR = 'regular', _('Regular')
    MALA = 'mala', _('Mala')


class SistemaRiegoChoices(models.TextChoices):
    GOTEO = 'goteo', _('Goteo')
    GRAVEDAD = 'gravedad', _('Gravedad')
    MICROASPERSION = 'microaspersión', _('Microaspersión')
    ASPERSION = 'aspersión', _('Aspersión')
    PIVOTE = 'pivote', _('Pivote')


class CondicionesSistemaRiegoChoices(models.TextChoices):
    BUENA = 'buena', _('Buena')
    REGULAR = 'regular', _('Regular')
    MALA = 'mala', _('Mala')


class SuperficieExternaChoices(models.TextChoices):
    ASFALTADA = 'asfaltada', _('Asfaltada')
    ENGRASONADA = 'engrasonada', _('Engrasonada')
    TIERRA_Y_GRAZON = 'tierra y grazon', _('Tierra y Grazon')
    FLUVIAL = 'fluvial', _('Fluvial')
    RIPIO = 'ripio', _('Ripio')
    OTROS = 'otros', _('Otros')


class SuperficieInternaChoices(models.TextChoices):
    ASFALTADA = 'asfaltada', _('Asfaltada')
    ENGRASONADA = 'engrasonada', _('Engrasonada')
    TIERRA_Y_GRAZON = 'tierra y grazon', _('Tierra y Grazon')
    FLUVIAL = 'fluvial', _('Fluvial')
    RIPIO = 'ripio', _('Ripio')
    OTROS = 'otros', _('Otros')


class Textura2Choices(models.TextChoices):
    ARCILLOSO = 'arcilloso', _('Arcilloso')
    ARENOSO = 'arenoso', _('Arenoso')
    FRANCO = 'franco', _('Franco')
    PH = 'ph', _('pH')


class VegetacionChoices(models.TextChoices):
    BAJA = 'baja', _('Baja')
    MEDIA = 'media', _('Media')
    ALTA = 'alta', _('Alta')


class Opcioneselectricidad(models.TextChoices):
    PLANTA = 'planta', _('Planta Eléctrica')
    GENERADOR = 'generador', _('Generador Eléctrico')
    TENIDO = 'tendido', _('Tendido Eléctrico')


class OpcionesAguasServidasChoices(models.TextChoices):
    POZO_SEPTICO = 'pozo_septico', _('Pozo séptico')
    CLOACAS = 'cloacas', _('Cloacas')
    OTROS = 'otros', _('Otros')


class Opcioneselectricidad(models.TextChoices):
    PLANTA = 'planta', _('Planta Eléctrica')
    GENERADOR = 'generador', _('Generador Eléctrico')
    TENIDO = 'tendido', _('Tendido Eléctrico')
