from django.urls import path

from Core.reportes.views import *

urlpatterns = [
    path('sale/', ReportesView.as_view(), name='sale_report'),
    path('misionesygrandesmisiones/', ReportesBaseMisionesView.as_view(),
         name='reportes_base_Misiones'),
    path('reporte_inpecciones/', ReportesInspec.as_view(), name='reporte_inpecciones'),

]
