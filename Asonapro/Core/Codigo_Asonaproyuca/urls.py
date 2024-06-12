from django.urls import path
# from .views import *

from . import views

urlpatterns = [
    path('create/', views.BaseCreateView.as_view(), name='codigo_create'),
]
