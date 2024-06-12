from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('app/dashboard/', Dashboard.as_view(), name='dashboard'),
    path('contactos/', Contactos.as_view(), name='contactos'),
]
