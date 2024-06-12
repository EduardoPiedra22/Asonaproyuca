
from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView, View
from Core.reportes.forms import ReportsForm
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from weasyprint import HTML, CSS
from django.template.loader import get_template

from Core.solicitud.models import *
from Core.solicitante.models import *
from Core.solicitud.forms import *


class ReportesView(TemplateView):
    template_name = 'report/reportes.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Solicitudes.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(fecha_registro__range=[
                                           start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.categoria.nombre,
                        s.id_solicitante.get_full_name(),
                        s.estatus,
                        s.fecha_registro.strftime('%Y-%m-%d'),
                    ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reportes de solicitudes'
        context['url'] = 'Reportes'
        context['title_body'] = 'Reportes de Solicitudes'
        context['enhead_body'] = 'Secretaria de Desarrollo Humano y Comunal'
        context['date_now'] = datetime.now()

        context['form'] = ReportsForm()
        return context


class ReportesBaseMisionesView(TemplateView):
    template_name = 'report/reportes_misiones.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = BaseGrandesMisiones.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(fecha_registro__range=[
                                           start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.nombre,
                        s.responsable.get_full_name(),
                        s.municipio,
                        s.nombre_p,
                        s.nombre_c,
                    ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reportes de Misiones y Grandes Misiones'
        context['url'] = 'Reportes de Misiones y Grandes Misiones'
        context['title_body'] = 'Reportes de Misiones y Grandes Misiones'
        context['date_now'] = datetime.now()
        context['form'] = ReportsForm()
        return context


# REPORTES DE INSPECCIONES
class ReportesInspec(TemplateView):
    template_name = 'report/reportesInspec.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Sembradores.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(fecha_registro__range=[
                                           start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.username,
                        s.cedula,
                        s.cedula_agraria,
                        s.codigo_asonaproyuca,
                        s.get_full_name,
                        s.email 
                        ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reportes de las Inspecciones'
        context['url'] = 'Reportes'
        context['title_body'] = 'Reportes de las Inspecciones'
        context['enhead_body'] = 'Secretaria de Desarrollo Humano y Comunal'
        context['date_now'] = datetime.now()
        context['entity'] = 'Reportes'
        context['form'] = ReportsForm()
        return context
