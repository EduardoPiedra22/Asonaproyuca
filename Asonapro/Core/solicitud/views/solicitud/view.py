from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *

from Core.solicitud.forms import*
from Core.mixins import*
from Core.solicitud.models import*
# Create your views here.

class SolicitudesListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
	model = Solicitudes
	context_object_name = 'Solicitudes'
	permission_required = 'view_solicitudes'
	template_name = "solicitud/Lista_Solicitudes.html"

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
				for i in Solicitudes.objects.all():
					item = i.toJSON()
					item['position'] = position
					data.append(item)

					position +=1
			else:
				data['error'] = 'Ha ocurrido un error'

		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data, safe=False)

	    
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Lista de Solicitudes'
		context['url'] = 'Solicitudes'
		context['title_body'] = 'Listado de Solicitudes'
		context['date_now'] = datetime.now()
		context['create_url'] = reverse_lazy('solicitud:Solicitudes_crear')
		context['list_url'] = reverse_lazy('solicitud:Solicitudes_lista')
		return context


class SolicitudesCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
	model = Solicitudes
	form_class = SolicitudesForm
	template_name = 'solicitud/Solicitudes_Form.html'
	permission_required = 'add_solicitudes'
	success_url = reverse_lazy('solicitud:Solicitudes_lista')


	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'add':
				form = self.get_form()
				data = form.save()
			else:
				data['error'] = 'No ha ingresado a ninguna opción'
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Formulario de Solicitudes'
		context['url'] = 'Solicitudes'
		context['title_body'] = 'Crear una Solicitud'
		context['date_now'] = datetime.now()
		context['list_url'] = reverse_lazy('solicitud:Solicitudes_lista')
		context['action'] = 'add'
		return context


class SolicitudesUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
	model = Solicitudes
	form_class = SolicitudesForm
	template_name = 'solicitud/Solicitudes_Form.html'
	permission_required = 'change_solicitudes'
	success_url = reverse_lazy('solicitud:Solicitudes_lista')

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
		context['title'] = 'Editar Solicitudes'
		context['url'] = 'Solicitudes'
		context['title_body'] = 'Editar una Solicitud'
		context['date_now'] = datetime.now()
		context['list_url'] = reverse_lazy('solicitud:Solicitudes_lista')
		context['action'] = 'edit'
		return context



class SolicitudesDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
	model = Solicitudes
	template_name = 'solicitud/Solicitudes_Delete.html'
	permission_required = 'delete_solicitudes'
	success_url = reverse_lazy('solicitud:Solicitudes_lista')

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
		context['title'] = 'Eliminar Solicitud'
		context['url'] = 'Solicitudes'
		context['date_now'] = datetime.now()
		context['title_body'] = 'Eliminar una Solicitud'
		context['list_url'] = reverse_lazy('solicitud:Solicitudes_lista')
		return context



class SolicitudChangeEstatusView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
	model = Solicitudes
	form_class = SolicitudesForm2
	template_name = 'solicitud/Solicitudes_Form.html'
	permission_required = 'view_solicitudes','change_solicitudes','delete_solicitudes','add_solicitudes'
	success_url = reverse_lazy('solicitud:Solicitudes_lista')

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
		context['title'] = 'Aprobacion de Solicitudes'
		context['url'] = 'Solicitudes'
		context['title_body'] = 'Aprobacion de una Solicitud'
		context['date_now'] = datetime.now()
		context['list_url'] = reverse_lazy('solicitud:Solicitudes_lista')
		context['action'] = 'edit'
		return context
