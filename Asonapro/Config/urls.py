"""Master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('Core.app.urls', 'app'), namespace='app')),
    path('login/', include(('Core.login.urls', 'login'), namespace='login')),
    path('sold/', include(('Core.solicitud.urls', 'solicitud'), namespace='solicitud')),
    path('solt/', include(('Core.solicitante.urls',
         'solicitante'), namespace='solicitante')),
    path('user/', include(('Core.User.urls', 'user'), namespace='user')),
    path('report/', include(('Core.reportes.urls', 'reporte'), namespace='reporte')),
    path('chat/', include(('Core.chats.urls', 'chat'), namespace='chat')),
    path('codigo/', include(('Core.Codigo_Asonaproyuca.urls', 'codigo'), namespace='codigo')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
