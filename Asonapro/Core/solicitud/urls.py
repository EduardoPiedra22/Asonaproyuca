from django.urls import path
from Core.solicitud.views.categorias.view import *
from Core.solicitud.views.solicitud.view import *
from Core.solicitud.views.test.view import *
from Core.solicitud.views.misiones.view import *
from Core.solicitud.views.inspeccion.view import *
from Core.solicitud.views.seguimiento.views import *
#from Core.solicitud.views.reportes.views import *
#from Core.solicitud.CrearPdf import *
#from Core.solicitud.Crearpdf2 import *
#from Core.solicitud.views.reportes.views import crear_pdf
#from Core.solicitud.views.reportes.views2 import generarpdf



urlpatterns = [
    path('solicitudes/', Base.as_view(), name='base'),
    path('lista/', SolicitudesListView.as_view(), name='Solicitudes_lista'),
    path('add/', SolicitudesCreateView.as_view(), name='Solicitudes_crear'),
    path('update/<int:pk>/', SolicitudesUpdateView.as_view(),
         name='Solicitudes_editar'),
    path('change/<int:pk>/', SolicitudChangeEstatusView.as_view(),
         name='Solicitudes_Change_estatus'),
    path('delete/<int:pk>/', SolicitudesDeleteView.as_view(),
         name='Solicitudes_eliminar'),
    path('catg/lista/', CategoriasListView.as_view(), name='Categorias_lista'),
    path('catg/add/', CategoriasCreateView.as_view(), name='Categorias_crear'),
    path('catg/update/<int:pk>/', CategoriasUpdateView.as_view(),
         name='Categorias_editar'),
    path('catg/delete/<int:pk>/', CategoriasDeleteView.as_view(),
         name='Categorias_eliminar'),

    # Base de Misiones y Grandes Misones
    path('basemisiones/lista/', BaseMisionesListView.as_view(),
         name='Lista_Base_Misiones'),
    path('basemisiones/add/', BaseMisionesCreateView.as_view(),
         name='Add_Base_Misiones'),
    path('basemisiones/update/<int:pk>/',
         BaseMisionesUpdateView.as_view(), name='Update_Base_Misiones'),
    path('basemisiones/delete/<int:pk>/',
         BaseMisionesDeleteView.as_view(), name='Delete_Base_Misiones'),

    # Encargado de Misiones
    path('encargados/lista/', EncargadosListView.as_view(), name='Lista_Encargados'),
    path('encargados/add/', EncargadosCreateView.as_view(), name='Add_Encargados'),
    path('encargados/update/<int:pk>/',
         EncargadosUpdateView.as_view(), name='Update_Encargados'),
    path('encargados/delete/<int:pk>/',
         EncargadosDeleteView.as_view(), name='Delete_Encargados'),

    # test
    path('test/', TestView.as_view(), name='Test_selec2'),


    # INSPECCIONES
    path('inspeccion/add/',
         InspeccionCreateView.as_view(), name='Crear_inspeccion'),
      
    path('inspeccion/list/',
         InspeccionListView.as_view(), name='Listar_inspeccion'),
    path('inspeccion/update/<int:pk>/',
         InspeccionUpdateView.as_view(), name='Update_inspeccion'),
#    path('inspeccion/list/',
#         ListarInspeccionesView.as_view(), name='Listar_inspeccion'),


    # SEGUIMIENTOS
    path('seguimientos_usuario_tecnico/', SeguimientoUserListView.as_view(), name='ver_seguimientos_usuario_tecnico'),
    path('seguimientos_usuario_sembrador/', SeguimientoUsersembrador.as_view(), name='ver_seguimientos_usuario_sembrador'),
    path('seguimientos/add/',
         SeguimientoCreateView.as_view(), name='Crear_seguimiento'),
    path('seguimientos/list/',
         SeguimientoListView.as_view(), name='Listar_seguimiento'),
    path('seguimientos/update/<int:pk>/',
         SeguimientoUpdateView.as_view(), name='Update_seguimiento'),
    path('seguimientos/delete/<int:pk>/',
         SeguimientoDeleteView.as_view(), name='Delete_seguimiento'),



    # REPORTES
   # path('generar_pdf/<int:id>/', generar_pdf, name='generar_pdf'),
   # path('generarpdf/<int:seguimiento_id>/', generarpdf, name='generar_pdf2'),

]




