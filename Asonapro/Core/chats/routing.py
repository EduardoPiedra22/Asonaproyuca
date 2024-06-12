from django.urls import path
from Core.chats.consumers import PrivateChatConsumer

websocket_urlpatterns = [
    path('ws/<int:id>/', PrivateChatConsumer.as_asgi()),
]