from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Codigo


class CodigoForm(forms.ModelForm):
    class Meta:
        model = Codigo
        fields = '__all__'
