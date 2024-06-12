from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View

from .models import Codigo
from .forms import CodigoForm


class BaseCreateView(View):
    model = Codigo
    form_class = CodigoForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'codigo_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.object = form.save()
            data = {
                'codigo': self.object.codigo,
            }
            return JsonResponse(data, status=201)
        else:
            return JsonResponse({'message': 'Error al crear el codigo.'}, status=400)
