from django.urls import path
from django.conf import settings

from Core.User.views import *
from django.conf.urls.static import static

urlpatterns = [          
     # USUARIO ADMIN
     path('lista/', UserListView.as_view(), name='User_lista'),
     path('add/', UserCreateView.as_view(), name='User_crear'),
     path('update/<int:pk>/', UserUpdateView.as_view(), name='User_editar'),
     path('delete/<int:pk>/', UserDeleteView.as_view(), name='User_delete'),
     path('change/group/<int:pk>/', UserChangeGropus.as_view(), name='user_change_group'),
     path('profile/', UserProfileView.as_view(), name='User_profile'),
     path('change/password/', UserChangePasswordView.as_view(),name='User_change_password'),

    # PERFIL SEMBRADOR}

     path('profileSembrador/', DashboardS.as_view(), name='profile_s'),
     path('profile/Sembrador/<int:pk>/', SembradoresProfileView.as_view(),name='Sembrador_profile'),

     path('add/sembradores/', CrearSembradorView.as_view(),name='Sembrador_crear'),
     path('lista/sembradores/', ListarSembradorView.as_view(),name='Sembradores_Listar'),


    # PERFIL TECNICO
     path('profileTecnico/', Dashboard.as_view(), name='profile'),
     path('profile/tecnico/<int:pk>/',TecnicoProfileView.as_view(), name='Tecnico_profile'),
     path('add/tecnico/', CrearTecnicoView.as_view(), name='Tecnico_crear'),
     path('lista/tecnico/', ListarTecnicosView.as_view(), name='Tecnico_Listar'),

     path('scannqr/', simple_view, name='scannqr'),

     ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
