from datetime import datetime
from typing import Any
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *

from Core.reportes.forms import*
from Core.solicitud.forms import*
from Core.mixins import*
from Core.solicitud.models import*


class SeguimientoListView(LoginRequiredMixin, ListView):
    model = Seguimiento
    template_name = 'seguimiento/seguimiento_Lista.html'
    permission_required = 'view_seguimiento'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                position = 1
                for seguimiento in Seguimiento.objects.all():
                    item = seguimiento.toJSON()
                    item['position'] = position
                    data.append(item)
                    position += 1
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    # Método para obtener los datos del contexto (puede variar según tu lógica)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Seguimientos'
        context['url'] = 'Seguimientos'
        context['title_body'] = 'Listado de Seguimientos'
        context['date_now'] = datetime.now()
        context['create_url'] = reverse_lazy('solicitud:Crear_seguimiento')
        context['list_url'] = reverse_lazy('solicitud:Listar_seguimiento')

        return context


class SeguimientoCreateView(CreateView):
    model = Seguimiento
    form_class = SeguimientoForm
    permission_required = 'add_seguimiento'
    template_name = 'form.html'
    success_url = reverse_lazy('solicitud:Listar_seguimiento')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Formulario de Seguimiento'
        context['url'] = 'Seguimiento'
        context['title_body'] = 'Formulario de Seguimiento'
        context['list_url'] = reverse_lazy('solicitud:Listar_seguimiento')
        context['action'] = 'add'
        return context


class SeguimientoUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
	model = Seguimiento
	form_class = SeguimientoForm
	template_name = 'seguimiento/seguimiento_form.html'
	permission_required = 'change_Seguimiento'
	success_url = reverse_lazy('solicitud:Listar_seguimiento')

	def dispatch(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'edit':
				form = self.get_form()
				data = form.save()
			else:
				data['error'] = 'No ha ingresado a ninguna opción'
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Editar Seguimiento'
		context['url'] = 'Seguimiento'
		context['title_body'] = 'Editar un Seguimiento'
		context['date_now'] = datetime.now()
		context['list_url'] = reverse_lazy('solicitud:Listar_seguimiento')
		context['action'] = 'edit'
		return context


class SeguimientoDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
	model = Seguimiento
	template_name = 'seguimiento/seguimiento_Delete.html'
	permission_required = 'delete_Seguimiento'
	success_url = reverse_lazy('solicitud:Listar_seguimiento')

	def dispatch(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super().dispatch(request, *args, **kwargs)


	def post(self, request, *args, **kwargs):
		data = {}
		try:
			self.object.delete()
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Eliminar Seguimiento'
		context['url'] = 'Seguimiento'
		context['date_now'] = datetime.now()
		context['title_body'] = 'Eliminar una Seguimiento'
		context['list_url'] = reverse_lazy('solicitud:Listar_seguimiento')
		return context



class SeguimientoUserListView(LoginRequiredMixin, TemplateView):
    template_name = 'seguimiento/ver_seguimientos_usuario.html'

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
                # Obtén el usuario actual del request
                user = request.user

                # Filtra los seguimientos solo para el usuario actual
                search = Seguimiento.objects.filter(tecnico=user)
                if len(start_date) and len(end_date):
                    search = search.filter(fecha_visita__range=[
                                           start_date, end_date])
                for s in search:
                    data.append([
                        s.seguimiento_id,
                        s.Sembrador_user.get_full_name(),
                        s.tecnico.get_full_name(),
                        s.nombre_persona_atendio,
                        s.cedula,
                        s.tlf,
                        s.fecha_visita.strftime('%Y-%m-%d'),
                        s.fecha_proxima_visita.strftime('%Y-%m-%d'),
                        s.motivo_visita,
                        s.lote1,
                        s.lote2,
                        s.lote3,
                        s.lote4,
                        s.edad_cultivo,
                        s.superficie_up,
                        s.superficie_preparada,
                        s.superficie_sembrada,
                        s.rubro_sembrado,
                        s.semilla_variedad,
                        s.realizar_recomendacion,
                        s.fecha_estimada_cosecha.strftime('%Y-%m-%d'),
                        s.superficie_por_consechar,
                        s.superficie_cosechada,
                        s.superficie_perdida,
                        s.superficie_efectiva,
                        s.estimacion_del_redimiento,
                        s.redimiento,
                        s.redimiento_total,
                        s.dar_continuidad,
                        s.descripcion,
                        s.coordenadas_norte,
                        s.coordenadas_sur,
                                               
                    ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tus Seguimiento'
        context['url'] = 'Seguimiento'
        context['date_now'] = datetime.now()
        context['title_body'] = 'Lista de Tus Seguimiento'
        context['list_url'] = reverse_lazy('solicitud:Listar_seguimiento')
        context['form'] = ReportsForm()

        return context
    


class SeguimientoUsersembrador(LoginRequiredMixin, TemplateView):
    template_name = 'seguimiento/ver_seguimientos_usuario.html'

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
                # Obtén el usuario actual del request
                user = request.user

                # Filtra los seguimientos solo para el usuario actual
                search = Seguimiento.objects.filter(Sembrador_user=user)
                if len(start_date) and len(end_date):
                    search = search.filter(fecha_visita__range=[
                                           start_date, end_date])
                for s in search:
                    data.append([
                        s.seguimiento_id,
                        s.Sembrador_user.get_full_name(),
                        s.tecnico.get_full_name(),
                        s.nombre_persona_atendio,
                        s.cedula,
                        s.tlf,
                        s.fecha_visita.strftime('%Y-%m-%d'),
                        s.fecha_proxima_visita.strftime('%Y-%m-%d'),
                        s.motivo_visita,
                        s.lote1,
                        s.lote2,
                        s.lote3,
                        s.lote4,
                        s.edad_cultivo,
                        s.superficie_up,
                        s.superficie_preparada,
                        s.superficie_sembrada,
                        s.rubro_sembrado,
                        s.semilla_variedad,
                        s.realizar_recomendacion,
                        s.fecha_estimada_cosecha.strftime('%Y-%m-%d'),
                        s.superficie_por_consechar,
                        s.superficie_cosechada,
                        s.superficie_perdida,
                        s.superficie_efectiva,
                        s.estimacion_del_redimiento,
                        s.redimiento,
                        s.redimiento_total,
                        s.dar_continuidad,
                        s.descripcion,
                        s.coordenadas_norte,
                        s.coordenadas_sur,
                                               
                    ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tus Seguimiento'
        context['url'] = 'Seguimiento'
        context['date_now'] = datetime.now()
        context['title_body'] = 'Lista de Tus Seguimiento'
        context['list_url'] = reverse_lazy('solicitud:Listar_seguimiento')
        context['form'] = ReportsForm()

        return context