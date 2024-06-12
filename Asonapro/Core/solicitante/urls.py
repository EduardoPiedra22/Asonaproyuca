from django.urls import path
from Core.solicitante.views.solicitantes.view import*


urlpatterns = [
    # CRUD
    path('lista/', SolicitanteListView.as_view(), name = 'Solicitante_Lista'),
    path('add/', SolicitanteCreateView.as_view(), name = 'Solicitante_Crear'),
    path('update/<int:pk>/', SolicitanteUpdateView.as_view(), name = 'Solicitante_editar'),
    path('delete/<int:pk>/', SolicitanteDeleteView.as_view(), name = 'Solicitante_eliminar'),
    
    ]