from django.contrib import admin
from .models import *
# Register your models here.

class AdminSolicitantes(admin.ModelAdmin):
	list_display = ['id','fecha_registro','cedula','nombre','apellido','telefono','correo_electronico','direccion']


admin.site.register(Solicitante, AdminSolicitantes)

