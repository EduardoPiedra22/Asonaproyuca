from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, Field, HTML

from .models import *
from .choicesV import *
from .models import Seguimiento
from django.forms import NumberInput

class CategoriasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='form-group col-md-6'),
                Column('descipcion', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
        )

    class Meta:
        model = Categorias
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce tipo de ayuda'}),
            'descipcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce descripcion de ayuda'}),
        }
        exclude = ['user_creation', 'user_update']

    def save(self):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class SolicitudesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('categoria', css_class='form-group col-md-6'),
                Column('id_solicitante', css_class='form-group col-md-6'),
                Column('descripcion', css_class='form-group col-md-12'),
                css_class='form-row'
            ),
        )

    class Meta:
        model = Solicitudes
        fields = '__all__'
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control select2 mt-3'}),
            'id_solicitante': forms.Select(attrs={'class': 'form-control select2 mt-3'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows': 3, 'cols': 3}),
        }
        exclude = ['user_creation', 'user_update']

    def save(self):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class SolicitudesForm2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('estatus', css_class='form-group col-md-12'),
                Column('descripcion_motivo', css_class='form-group col-md-12'),
                css_class='form-row'
            ),
        )

    class Meta:
        model = Solicitudes
        fields = '__all__'
        widgets = {
            'estatus': forms.Select(attrs={'class': 'form-control select2 mt-3'}),
            'descripcion_motivo': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows': 3, 'cols': 3}),
        }
        exclude = ['id_solicitante', 'categoria',
                   'descripcion', 'user_creation', 'user_update']

    def save(self):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class TestForm(forms.Form):
    categories = forms.ModelChoiceField(queryset=Categorias.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    products = forms.ModelChoiceField(queryset=Solicitudes.objects.none(), widget=forms.Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    # search = CharField(widget=TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Ingrese una descripción'
    # }))

    search = forms.ModelChoiceField(queryset=Solicitudes.objects.none(), widget=forms.Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))


class EncargadoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('cedula', css_class='form-group col-md-4'),
                Column('nombre', css_class='form-group col-md-4'),
                Column('apellido', css_class='form-group col-md-4'),
                Column('fecha_nacimiento', css_class='form-group col-md-4'),
                Column('edad', css_class='form-group col-md-4'),
                Column('sexo', css_class='form-group col-md-4'),
                Column('codigo', css_class='form-group col-md-6'),
                Column('serial', css_class='form-group col-md-6'),
                Column('telefono', css_class='form-group col-md-12'),
                Column('email', css_class='form-group col-md-12'),
                css_class='form-row'
            ),
        )

    class Meta:
        model = EncargadoBaseMisiones
        fields = 'cedula', 'nombre', 'apellido', 'fecha_nacimiento', 'edad', 'sexo', 'telefono', 'email', 'codigo', 'serial'
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Introduce tus numero de Cedula'
                }),

            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Introduce tus Nombres'
                }),

            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Introduce tus Apellidos'
                }),


            'fecha_nacimiento': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }),

            'edad': forms.NumberInput(
                attrs={
                    'class': 'form-control',

                }),

            'sexo': forms.Select(
                attrs={
                    'class': 'form-control select2',

                }),

            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Telefono fijo o de Casa'
                }),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Introduce correo electronico'
                }),

            'codigo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Codigo',
                    'id': 'id_codigo'
                }),

            'serial': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Serial',
                    'id': 'id_codigo'
                }),
        }

    def save(self):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class BaseMisionesGrandeMisionesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='form-group col-md-4'),
                Column('responsable', css_class='form-group col-md-8'),
                Column('municipio', css_class='form-group col-md-4'),
                Column('nombre_p', css_class='form-group col-md-4'),
                Column('nombre_c', css_class='form-group col-md-4'),
                css_class='form-row'
            ),
        )

    class Meta:
        model = BaseGrandesMisiones
        fields = 'nombre', 'responsable', 'municipio', 'nombre_p', 'nombre_c'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control select2'}),
            'municipio': forms.Select(attrs={'class': 'form-control select2'}),
            'nombre_p': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_c': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def save(self):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class InspeccionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InspeccionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # Definir el diseño del formulario usando crispy-forms
        self.helper.layout = Layout(
            Row(
                Column('Sembrador_user', css_class='form-group col-md-4'),
                Column('tecnico', css_class='form-group col-md-4'),
                Column('nombre_unidad', css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Row(
                Column('direccion_unidad', css_class='form-group col-md-12'),
                Column('como_llegar', css_class='form-group col-md-12'),
                css_class='form-row'
            ),
            Row(
                Column('estado', css_class='form-group col-md-4'),
                Column('municipio', css_class='form-group col-md-4'),
                Column('parroquia', css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Row(
                Column('vive_en_unidad', css_class='form-group col-md-4'),
                Column('frecuencia_visita', css_class='form-group col-md-4'),
                Column('tenencia_de_tierra', css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Row(
                Column('vocacion_tierra', css_class='form-group col-md-4'),
                Column('vivienda', css_class='form-group col-md-4'),
                Column('material_vivienda', css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Row(
                Column('electricidad', css_class='form-group col-md-4'),
                Column('opciones_electricidad',
                       css_class='form-group col-md-4'),
                Column('transporte_insumo', css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Row(
                Column('opciones_transporte', css_class='form-group col-md-4'),
                Column('telefono', css_class='form-group col-md-4'),
                Column('opciones_telefono', css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Row(
                Column('gas', css_class='form-group col-md-4'),
                Column('opciones_gas', css_class='form-group col-md-4'),
                Column('aguas_blancas', css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Row(
                Column('opciones_aguas_blancas',
                       css_class='form-group col-md-4'),
                Column('superficie_total_up', css_class='form-group col-md-4'),
                Column('superficie_aprovechable_up',
                       css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Row(
                Column('superficie_gps', css_class='form-group col-md-4'),
                Column('drenaje_opciones', css_class='form-group col-md-4'),
                Column('condiciones_drenaje', css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Row(
                Column('fuentes_agua', css_class='form-group col-md-4'),
                Column('sistema_riego', css_class='form-group col-md-4'),
                Column('condiciones_sistema_riego',
                       css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Row(
                Column('superficie_externa', css_class='form-group col-md-4'),
                Column('superficie_interna', css_class='form-group col-md-4'),

                css_class='form-row'
            ),
            Row(
                Column('aguas_servidas', css_class='form-group col-md-4'),
                Column('opciones_aguas_servidas',
                       css_class='form-group col-md-4'),
                css_class='form-row'
            ),
        )

    class Meta:
        model = Inspeccion
        fields = '__all__'

        widgets = {
            'Sembrador_user': forms.Select(attrs={'class': 'form-control select2'}),
            'tecnico': forms.Select(attrs={'class': 'form-control select2'}),
            'nombre_unidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introdusca el Nombre de la Unidad de Produccion'}),
            'direccion_unidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introdusca la ubicacion de la unidad de Produccion'}),
            'como_llegar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introdusca la ruta detallada de como llegar a la unidad de produccion'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'id': 'estados'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control', 'id': 'municipios'}),
            'parroquia': forms.TextInput(attrs={'class': 'form-control', 'id': 'parroquiasCD'}),
            'vive_en_unidad': forms.NullBooleanSelect(),
            'frecuencia_visita': forms.Select(attrs={'class': 'form-control select2'}),
            'tenencia_de_tierra': forms.Select(attrs={'class': 'form-control select2'}),
            'vocacion_tierra': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'vivienda': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'material_vivienda': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'electricidad': forms.Select(attrs={'class': 'form-control select2'}),
            'opciones_electricidad': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'transporte_insumo': forms.Select(attrs={'class': 'form-control select2'}),
            'opciones_transporte': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'telefono': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Introdusca la ruta detallada de como llegar a la unidad de produccion'}),
            'opciones_telefono': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'gas': forms.Select(attrs={'class': 'form-control selec2'}),
            'opciones_gas': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'aguas_blancas': forms.Select(attrs={'class': 'form-control select2'}),
            'opciones_aguas_blancas': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'aguas_servidas': forms.Select(attrs={'class': 'form-control select2'}),
            'opciones_aguas_servidas': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'superficie_total_up': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introdusca la ruta detallada de como llegar a la unidad de produccion'}),
            'superficie_aprovechable_up': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introdusca la ruta detallada de como llegar a la unidad de produccion'}),
            'superficie_gps': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introdusca Medida de GPS'}),
            'drenaje_opciones': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'condiciones_drenaje': forms.Select(attrs={'class': 'form-control select2'}),
            'fuentes_agua': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'sistema_riego': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'condiciones_sistema_riego': forms.Select(attrs={'class': 'form-control select2'}),
            'superficie_externa': forms.Select(attrs={'class': 'form-control select2'}),
            'superficie_interna': forms.Select(attrs={'class': 'form-control select2'}),
        }

    def save(self):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class SeguimientoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('Sembrador_user', css_class='form-group col-md-4'),
                Column('tecnico', css_class='form-group col-md-4'),
                Column('nombre_persona_atendio',
                       css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Row(
                Column('cedula', css_class='form-group col-md-3'),
                Column('tlf', css_class='form-group col-md-3'),
                Column('fecha_visita', css_class='form-group col-md-3'),
                Column('fecha_proxima_visita',
                       css_class='form-group col-md-3'),

                css_class='form-row'
            ),
            Row(
                Column('motivo_visita', css_class='form-group col-md-3'),
                Column('edad_cultivo', css_class='form-group col-md-3'),
                Column('rubro_sembrado', css_class='form-group col-md-3'),
                Column('semilla_variedad', css_class='form-group col-md-3'),
                css_class='form-row'
            ),
            Row(
                Column('lote1', css_class='form-group col-md-3'),
                Column('lote2', css_class='form-group col-md-3'),
                Column('lote3', css_class='form-group col-md-3'),
                Column('lote4', css_class='form-group col-md-3'),
                css_class='form-row'
            ),
            Row(

                Column('superficie_up', css_class='form-group col-md-4'),
                Column('superficie_preparada',
                       css_class='form-group col-md-4'),
                Column('superficie_sembrada', css_class='form-group col-md-4'),

                css_class='form-row'
            ),
            Row(
                Column('realizar_recomendacion',
                       css_class='form-group col-md-3'),
                Column('fecha_estimada_cosecha',
                       css_class='form-group col-md-3'),
                Column('superficie_por_consechar',
                       css_class='form-group col-md-3'),
                Column('superficie_cosechada',
                       css_class='form-group col-md-3'),
                css_class='form-row'
            ),
            Row(
                Column('superficie_perdida', css_class='form-group col-md-4'),
                Column('superficie_efectiva', css_class='form-group col-md-4'),
                Column('estimacion_del_redimiento',
                       css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Row(
                Column('redimiento',
                       css_class='form-group col-md-4'),
                Column('redimiento_total', css_class='form-group col-md-4'),
                Column('dar_continuidad',
                       css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Row(
                Column('coordenadas_norte', css_class='form-group col-md-6'),
                Column('coordenadas_sur', css_class='form-group col-md-6'),
                Column('descripcion', css_class='form-group col-md-12'),

                css_class='form-row'
            ),
        )

    class Meta:
        model = Seguimiento
        fields = '__all__'
        widgets = {
            'nombre_persona_atendio': forms.TextInput(attrs={'placeholder': 'Nombre de la Persona que Atendio', 'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'placeholder': 'Cédula', 'class': 'form-control'}),
            'tlf': forms.TextInput(attrs={'placeholder': 'Telefono', 'class': 'form-control'}),

            'fecha_visita': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_proxima_visita': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_estimada_cosecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'motivo_visita': forms.Select(choices=MOTIVO_CHOICES, attrs={'class': 'form-control select2'}),
            'lote1': forms.TextInput(attrs={'placeholder': 'Lote 1', 'class': 'form-control'}),
            'lote2': forms.TextInput(attrs={'placeholder': 'Lote 2', 'class': 'form-control'}),
            'lote3': forms.TextInput(attrs={'placeholder': 'Lote 3', 'class': 'form-control'}),
            'lote4': forms.TextInput(attrs={'placeholder': 'Lote 4', 'class': 'form-control'}),
            'edad_cultivo': forms.TextInput(attrs={'placeholder': 'Edad del Cultivo', 'class': 'form-control'}),
            'superficie_up': forms.NumberInput(attrs={'placeholder': 'Superficie Up', 'class': 'form-control'}),
            'superficie_preparada': forms.NumberInput(attrs={'placeholder': 'Superficie Preparada', 'class': 'form-control'}),
            'superficie_sembrada': forms.NumberInput(attrs={'placeholder': 'Superficie Sembrada', 'class': 'form-control'}),
            'rubro_sembrado': forms.TextInput(attrs={'placeholder': 'Rubro Sembrado', 'class': 'form-control'}),
            'semilla_variedad': forms.TextInput(attrs={'placeholder': 'Semilla Variedad', 'class': 'form-control'}),
            'realizar_recomendacion': forms.Select(choices=RECOMENDACION, attrs={'class': 'form-control select2'}),
            'fecha_estimada_cosecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'superficie_por_consechar': forms.NumberInput(attrs={'placeholder': 'Superficie Por Consechar', 'class': 'form-control'}),
            'superficie_cosechada': forms.NumberInput(attrs={'placeholder': 'Superficie Cosechada', 'class': 'form-control'}),
            'superficie_perdida': forms.NumberInput(attrs={'placeholder': 'Superficie Perdida', 'class': 'form-control'}),
            'superficie_efectiva': forms.NumberInput(attrs={'placeholder': 'Superficie Efectiva', 'class': 'form-control'}),
            'estimacion_del_redimiento': forms.TextInput(attrs={'placeholder': 'Estimacion del Rendimiento', 'class': 'form-control'}),
            'redimiento': forms.TextInput(attrs={'placeholder': 'Rendimiento', 'class': 'form-control'}),
            'redimiento_total': forms.TextInput(attrs={'placeholder': 'Rendimiento Total', 'class': 'form-control'}),
            'dar_continuidad': forms.Select(choices=RECOMENDACION, attrs={'class': 'form-control select2'}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Descripcion', 'class': 'form-control'}),
            'coordenadas_norte': forms.TextInput(attrs={'placeholder': 'Coordenadas Norte', 'class': 'form-control'}),
            'coordenadas_sur': forms.TextInput(attrs={'placeholder': 'Coordenadas Sur', 'class': 'form-control'}),
            'tecnico': forms.Select(attrs={'placeholder': 'Tecnico', 'class': 'form-control select2'}),
            'Sembrador_user': forms.Select(attrs={'placeholder': 'Sembrador', 'class': 'form-control select2'}),
        }

    def save(self):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data