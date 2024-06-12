from django.http import JsonResponse
from datetime import datetime
from django.http import HttpResponseRedirect

from dal import autocomplete
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, FormView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from Core.mixins import *
from Core.solicitud.models import  Inspeccion
from Core.solicitud.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from Core.User.models import Sembradores, Tecnico


class InspeccionListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Inspeccion
    template_name = 'inspeccion/inspeccion_lista.html'
    permission_required = 'view_inspeccion'

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
                for inspeccion in Inspeccion.objects.all():
                    item = inspeccion.toJSON()
                    item['position'] = position
                    data.append(item)
                    position += 1
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listados de Inspecciones'
        context['url'] = 'Inspecciones'
        context['title_body'] = 'Listado de Inspecciones'
        context['date_now'] = datetime.now()
        context['create_url'] = reverse_lazy('solicitud:Crear_inspeccion')

        return context



class InspeccionCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Inspeccion
    form_class = InspeccionForm
        #fields = '__all__'
    template_name = 'form.html'
    permission_required = 'add_inspeccion'
    success_url = reverse_lazy('solicitud:Crear_inspeccion')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST.get('action', '')
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    inspeccion = form.save(commit=False)
                    inspeccion.tecnico = request.user  # Asignar el técnico al usuario logueado
                    inspeccion.save()
                    data['message'] = 'Inspección creada exitosamente'
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Formula de Inspeccion'
        context['url'] = 'Inspecciones'
        context['title_body'] = 'Formulario de Inspecciones'
        context['date_now'] = datetime.now()
        context['list_url'] = reverse_lazy('solicitud:Listar_inspeccion')
        context['action'] = 'add'
        return context
        
class InspeccionUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
	model = Inspeccion
	form_class = InspeccionForm
	template_name = 'inspeccion/inspeccion_form.html'
	permission_required = 'change_inspeccion'
	success_url = reverse_lazy('solicitud:Listar_inspeccion')

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
		context['title'] = 'Editar Inspeccion'
		context['url'] = 'Inspeccion'
		context['title_body'] = 'Editar un Inspeccion'
		context['date_now'] = datetime.now()
		context['list_url'] = reverse_lazy('solicitud:Listar_Inspeccion')
		context['action'] = 'edit'
		return context

