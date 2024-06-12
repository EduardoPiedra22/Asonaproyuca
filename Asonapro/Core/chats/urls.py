from django.urls import path
from Core.chats.views import *

app_name = 'chat'

urlpatterns = [
    path('chat/sala/', SalaListView.as_view(), name='sala'),
    path('dashboard/', dashboard, name='dashboard'),
    path('crear_publicacion/', crear_publicacion, name='crear_publicacion'),
]