"""
from django.views import View
from django.http import HttpResponse
from django.template import loader
from Core.solicitud.models import Inspeccion
from Core.User.models import Sembradores, Tecnico
from django.shortcuts import render
from Core.solicitud.CrearPdf import crear_pdf
from django.urls import reverse


def generar_pdf(request, id
                ):
    ruta_template = '/home/linuxlite/Desktop/Master/Core/solicitud/templates/reportes/hola.html'
    inspeccion_actual = Inspeccion.objects.get(id=id)
# sold/generar_pdf/1/
    sembrador_id = inspeccion_actual.Sembrador_user.id
    sembrador = Sembradores.objects.get(id=sembrador_id)

    tecnico_id = inspeccion_actual.tecnico.id
    tecnico = Tecnico.objects.get(id=tecnico_id)

    vocacion_tierra = inspeccion_actual.vocacion_tierra.all()

    material_vivienda = inspeccion_actual.material_vivienda.all()

    opciones_electricidad = inspeccion_actual.opciones_electricidad.all()

    opciones_transporte = inspeccion_actual.opciones_transporte.all()

    opciones_telefono = inspeccion_actual.opciones_telefono.all()

    opciones_gas = inspeccion_actual.opciones_gas.all()

    opciones_aguas_blancas = inspeccion_actual.opciones_aguas_blancas.all()

    opciones_aguas_servidas = inspeccion_actual.opciones_aguas_servidas.all()

    fuentes_agua = inspeccion_actual.fuentes_agua.all()

    drenaje_opciones = inspeccion_actual.drenaje_opciones.all()

    sistema_riego = inspeccion_actual.sistema_riego.all()
    url = reverse('solicitud:generar_pdf', kwargs={'id': id})


    info = {
        'sembrador': sembrador,
        'tecnico': tecnico,
        'inspeccion_actual': inspeccion_actual,
        'vocacion_tierra': vocacion_tierra,
        'material_vivienda': material_vivienda,
        'opciones_electricidad': opciones_electricidad,
        'opciones_transporte': opciones_transporte,
        'opciones_telefono': opciones_telefono,
        'opciones_gas': opciones_gas,
        'opciones_aguas_blancas': opciones_aguas_blancas,
        'opciones_aguas_servidas': opciones_aguas_servidas,
        'fuentes_agua': fuentes_agua,
        'drenaje_opciones': drenaje_opciones,
        'sistema_riego': sistema_riego

    }

    # Llama a la función para generar el PDF
    crear_pdf(ruta_template, info)

    # Devuelve una respuesta HTTP apropiada (puede ser un redireccionamiento o un mensaje de éxito)
    with open('/home/linuxlite/Desktop/Master/Core/solicitud/templates/reportes/hola.pdf', 'rb') as pdf_file:
        response = HttpResponse(
            pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=hola.pdf'
        return response


def vista_previa_pdf(request):
    pdf_url = '/home/linuxlite/Desktop/Master/Core/solicitud/templates/reportes/hola.pdf'
    return render(request, 'hola.html', {'pdf_url': pdf_url})
"""