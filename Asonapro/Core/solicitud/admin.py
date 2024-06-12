from django.contrib import admin
from .models import *
# Register your models here.


class AdminCategorias(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descipcion', 'user_creation',
                    'date_creation', 'user_update', 'date_updated']

    search_fields = ['nombre']


class AdminSolicitudes(admin.ModelAdmin):
    list_display = ['id', 'categoria',
                    'id_solicitante', 'estatus', 'fecha_registro']


class AdminBaseGrandesMisiones(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'responsable',
                    'municipio', 'nombre_p', 'nombre_c']


class AdminEncargadoBaseMisiones(admin.ModelAdmin):
    list_display = ['id', 'cedula', 'fecha_nacimiento', 'nombre',
                    'apellido', 'edad', 'sexo', 'email', 'telefono', 'codigo', 'serial']


admin.site.register(Categorias, AdminCategorias)
admin.site.register(Solicitudes, AdminSolicitudes)


admin.site.register(BaseGrandesMisiones, AdminBaseGrandesMisiones)
admin.site.register(EncargadoBaseMisiones, AdminEncargadoBaseMisiones)
admin.site.register(Inspeccion)
admin.site.register(FuenteAgua)
admin.site.register(OpcionDrenaje)
admin.site.register(OpcionesAguaBlancas)
admin.site.register(OpcionesAguasServidas)
admin.site.register(OpcionesTelefono)
admin.site.register(OpcionesGas)
admin.site.register(OpcionesElectricidad)
admin.site.register(OpcionesTransporte)
admin.site.register(VocacionTierra)
admin.site.register(Material_vivienda)
admin.site.register(SistemaRiego)
admin.site.register(Seguimiento)
