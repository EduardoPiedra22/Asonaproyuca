from datetime import datetime
from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import *

from Core.solicitud.models import Solicitudes

from random import randint
# Create your views here.


class Index(TemplateView):
    template_name = "app/body.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'BIENBENIDOS'

        return context


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        request.user.get_group_session()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        context['title_body'] = 'Dashboard'
        context['user_is_tecnico'] = self.request.user.groups.filter(
            name='Tecnicos').exists()
        context['user_is_sembrador'] = self.request.user.groups.filter(
            name='Sembradores').exists()
        return context


class Contactos(LoginRequiredMixin, TemplateView):
    template_name = "contactos.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        request.user.get_group_session()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contactos '
        context['title_body'] = 'Contactos'
        context['url'] = 'Contactos'
        return context
