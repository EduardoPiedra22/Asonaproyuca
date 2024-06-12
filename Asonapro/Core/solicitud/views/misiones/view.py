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



class BaseMisionesListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
	model = BaseGrandesMisiones
	template_name = "misiones/Lista_Grandes_Misiones.html"
	permission_required = 'view_basegrandesmisiones'

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'searchdata':
				data = []
				position = 1 # Contador para crear el orden de los id o Pk
				for i in BaseGrandesMisiones.objects.all():
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
		context['title'] = 'Lista de Fincas en Produccion'
		context['url'] = 'Fincas'
		context['title_body'] = 'Lista de fincas en Produccion'
		context['date_now'] = datetime.now()
		context['create_url'] = reverse_lazy('solicitud:Add_Base_Misiones')
		context['list_url'] = reverse_lazy('solicitud:Lista_Base_Misiones')

		return context



class BaseMisionesCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
	model = BaseGrandesMisiones
	form_class = BaseMisionesGrandeMisionesForm
	template_name = 'misiones/Base_Misiones_Form.html'
	permission_required = 'add_basegrandesmisiones'
	success_url = reverse_lazy('solicitud:Lista_Base_Misiones')
	

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
		context['title'] = 'Formulario de Fincas para Produccion'
		context['url'] = 'Fincas'
		context['title_body'] = 'Formulario de Fincas para Produccion'
		context['list_url'] = reverse_lazy('solicitud:Lista_Base_Misiones')
		context['action'] = 'add'
		return context

class BaseMisionesUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
	model = BaseGrandesMisiones
	form_class = BaseMisionesGrandeMisionesForm
	template_name = 'misiones/Base_Misiones_Form.html'
	permission_required = 'change_basegrandesmisiones'
	success_url = reverse_lazy('solicitud:Lista_Base_Misiones')

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
		context['title'] = 'Editar Fincas en Produccion'
		context['url'] = 'Fincas para Produccion'
		context['title_body'] = 'Editar Fincas en Produccion'
		context['date_now'] = datetime.now()
		context['list_url'] = reverse_lazy('solicitud:Lista_Base_Misiones')
		context['action'] = 'edit'
		return context



class BaseMisionesDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
	model = BaseGrandesMisiones
	template_name = 'delete.html'
	permission_required = 'delete_basegrandesmisiones'
	success_url = reverse_lazy('solicitud:Lista_Base_Misiones')

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
		context['title'] = 'Eliminar Fincas en Produccion'
		context['url'] = 'Fincas para Produccion'
		context['date_now'] = datetime.now()
		context['title_body'] = 'Eliminar una Fincas en Produccion'
		context['list_url'] = reverse_lazy('solicitud:Lista_Base_Misiones')
		return context







class EncargadosListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
	model = EncargadoBaseMisiones
	template_name = "misiones/Lista_Encargados.html"
	permission_required = 'view_encargadobasemisiones'

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'searchdata':
				data = []
				position = 1 # Contador para crear el orden de los id o Pk
				for i in EncargadoBaseMisiones.objects.all():
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
		context['title'] = 'Lista de Encargados'
		context['url'] = 'Encargados'
		context['title_body'] = 'Lista de Encargados'
		context['date_now'] = datetime.now()
		context['create_url'] = reverse_lazy('solicitud:Add_Encargados')
		context['list_url'] = reverse_lazy('solicitud:Lista_Encargados')

		return context



class EncargadosCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
	model = EncargadoBaseMisiones
	form_class = EncargadoForm
	template_name = 'misiones/Encargado_Form.html'
	permission_required = 'add_encargadobasemisiones'
	success_url = reverse_lazy('solicitud:Lista_Encargados')
	

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
		context['title'] = 'Formulario de Encargados'
		context['url'] = 'Encargados'
		context['title_body'] = 'Formulario de Encargados'
		context['list_url'] = reverse_lazy('solicitud:Lista_Encargados')
		context['action'] = 'add'
		return context



class EncargadosUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
	model = EncargadoBaseMisiones
	form_class = EncargadoForm
	template_name = 'misiones/Encargado_Form.html'
	permission_required = 'change_encargadobasemisiones'
	success_url = reverse_lazy('solicitud:Lista_Encargados')

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
		context['title'] = 'Editar Encargado'
		context['url'] = 'Encargados'
		context['title_body'] = 'Editar Encargado'
		context['date_now'] = datetime.now()
		context['list_url'] = reverse_lazy('solicitud:Lista_Encargados')
		context['action'] = 'edit'
		return context



class EncargadosDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
	model = Solicitudes
	template_name = 'delete.html'
	permission_required = 'delete_encargadobasemisiones'
	success_url = reverse_lazy('solicitud:Lista_Encargados')

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
		context['title'] = 'Eliminar Encargados'
		context['url'] = 'Encargados'
		context['date_now'] = datetime.now()
		context['title_body'] = 'Eliminar un Encargados'
		context['list_url'] = reverse_lazy('solicitud:Lista_Encargados')
		return context
