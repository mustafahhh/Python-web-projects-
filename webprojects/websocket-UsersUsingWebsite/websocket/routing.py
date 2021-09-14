from django.urls import path 

from .consumers import OnlineUsers

ws_urlpatterns = [
    path('websocket/',OnlineUsers.as_asgi())

]


