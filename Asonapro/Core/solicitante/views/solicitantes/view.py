from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *

from Core.solicitante.forms import *
from Core.mixins import *
from Core.solicitante.models import *
# Create your views here.


class SolicitanteListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Solicitante
    template_name = "solicitante/Lista_Solicitantes.html"
    permission_required = 'view_solicitante'

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
                for i in Solicitante.objects.all():
                    item = i.toJSON()
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
        context['title'] = 'Lista de Solicitantes'
        context['url'] = 'Solicitantes'
        context['title_body'] = 'Listado de Solicitantes'
        context['date_now'] = datetime.now()
        context['create_url'] = reverse_lazy('solicitante:Solicitante_Crear')
        context['list_url'] = reverse_lazy('solicitante:Solicitante_Lista')
        context['action'] = 'add'
        return context


class SolicitanteCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Solicitante
    form_class = SolicitanteForm
    template_name = 'solicitante/Solicitante_Form.html'
    permission_required = 'add_solicitante'
    success_url = reverse_lazy('solicitante:Solicitante_Lista')

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
        context['title'] = 'Formulario de Solicitante'
        context['url'] = 'Solicitante'
        context['title_body'] = 'Registrar Solicitante'
        context['list_url'] = reverse_lazy('solicitante:Solicitante_Lista')
        context['action'] = 'add'
        return context


class SolicitanteUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Solicitante
    form_class = SolicitanteForm
    template_name = 'solicitante/Solicitante_Form.html'
    permission_required = 'change_solicitante'
    success_url = reverse_lazy('solicitante:Solicitante_Lista')

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
        context['title'] = 'Editar Solicitante'
        context['url'] = 'Solicitante'
        context['title_body'] = 'Crear un nuevo Solicitante'
        context['list_url'] = reverse_lazy('solicitante:Solicitante_Lista')
        context['action'] = 'edit'
        return context


class SolicitanteDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Solicitante
    template_name = 'solicitante/Solicitante_Delete.html'
    permission_required = 'delete_solicitante'
    success_url = reverse_lazy('solicitante:Solicitante_Lista')

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
        context['title'] = 'Eliminar Solicitante'
        context['url'] = 'Solicitante'
        context['title_body'] = 'Eliminar Solicitante'
        context['list_url'] = reverse_lazy('solicitante:Solicitante_Lista')
        return context
