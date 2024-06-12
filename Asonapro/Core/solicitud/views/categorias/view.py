from datetime import datetime
from django.shortcuts import render

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import *

from Core.solicitud.forms import *
from Core.mixins import *
from Core.solicitud.models import *
# Create your views here.


class Base(LoginRequiredMixin, TemplateView):
    template_name = "solicitud/base.html"
    permission_required = 'view_categorias', 'change_categorias', 'update_categorias', 'delete_categorias'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'get_graph_sales_year_month':
                data = {
                    'name': 'Porcentaje de solicitudes',
                    'showInLegend': False,
                    'colorByPoint': True,
                    'data': ""
                }
            else:
                data['error'] = 'Ha ocurrido un error'

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_graph_sales_year_month(self):
        data = []
        try:
            year = datetime.now().year
            for m in range(1, 13):
                total = Solicitudes.objects.filter(date_joined__year=year, date_joined__month=m).aggregate(
                    r=Coalesce(Sum('total'), 0)).get('r')
                data.append(float(total))
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Solicitudes'
        context['url'] = 'Solicitudes'
        context['title_body'] = 'Gestionar Solicitudes'
        context['graph_sales_year_month'] = self.get_graph_sales_year_month()
        return context


class CategoriasListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Categorias
    template_name = "category/Lista_Categorias.html"
    permission_required = 'view_categorias'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                position = 1  # Contador para crear el orden de los id o Pk
                for i in Categorias.objects.all():
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
        context['title'] = 'Lista de Categorias'
        context['url'] = 'Categorias'
        context['title_body'] = 'Listado de Tipos de Solicitudes'
        context['date_now'] = datetime.now()
        context['create_url'] = reverse_lazy('solicitud:Categorias_crear')
        context['list_url'] = reverse_lazy('solicitud:Categorias_lista')
        context['form'] = CategoriasForm()

        return context


class CategoriasCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Categorias
    form_class = CategoriasForm
    template_name = 'category/Categorias_Form.html'
    permission_required = 'add_categorias'
    success_url = reverse_lazy('solicitud:Categorias_lista')

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
        context['title'] = 'Formulario de Categorias'
        context['url'] = 'Categorias'
        context['title_body'] = 'Crear una Categotia'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['frmCateg'] = CategoriasForm()
        return context


class CategoriasUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Categorias
    form_class = CategoriasForm
    template_name = 'category/Categorias_Form.html'
    permission_required = 'change_categorias'
    success_url = reverse_lazy('solicitud:Categorias_lista')

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
        context['title'] = 'Editar Categorias'
        context['url'] = 'Categorias'
        context['title_body'] = 'Crear una Categotia'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class CategoriasDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Categorias
    template_name = 'category/Categorias_Delete.html'
    permission_required = 'delete_categorias'
    success_url = reverse_lazy('solicitud:Categorias_lista')

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
        context['title'] = 'Eliminar Categorias'
        context['url'] = 'Categorias'
        context['title_body'] = 'Crear una Categotia'
        context['list_url'] = self.success_url
        return context
