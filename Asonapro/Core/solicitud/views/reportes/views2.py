"""
from django.views import View
from django.http import HttpResponse
from django.template import loader
from Core.solicitud.models import Seguimiento
from Core.User.models import Sembradores, Tecnico
from django.shortcuts import render
from Core.solicitud.Crearpdf2 import crear_pdf2

def generarpdf(request, seguimiento_id
               ):
    ruta_template = '/home/linuxlite/Desktop/Master/Core/solicitud/templates/reportes/seguimiento.html'
    seguimiento_actual = Seguimiento.objects.get(seguimiento_id=seguimiento_id)

    sembrador_id = seguimiento_actual.Sembrador_user.id
    sembrador = Sembradores.objects.get(id=sembrador_id)

    tecnico_id = seguimiento_actual.tecnico.id
    tecnico = Tecnico.objects.get(id=tecnico_id)

    info = {
        'sembrador': sembrador,
        'tecnico': tecnico,
        'sembrador_id': sembrador_id,
        'seguimiento_actual': seguimiento_actual

    }

    # Llama a la función para generar el PDF
    crear_pdf2(ruta_template, info)

    # Devuelve una respuesta HTTP apropiada (puede ser un redireccionamiento o un mensaje de éxito)
    with open('/home/linuxlite/Desktop/Master/Core/solicitud/templates/reportes/seguimiento.pdf', 'rb') as pdf_file:
        response = HttpResponse(
            pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=reporte.pdf'
        return response


def vista_previa_pdf(request):
    pdf_url = '/home/linuxlite/Desktop/Master/Core/solicitud/templates/reportes/seguimiento.pdf'
    # /home/linuxlite/Desktop/Master/Core/solicitud/templates/reportes/
    return render(request, 'seguimiento.html', {'pdf_url': pdf_url})
"""