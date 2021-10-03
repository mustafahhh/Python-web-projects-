from django.urls import path 

from .consumers import Chat

ws_urlpatterns = [
    path('websocket/<str:ID>/<str:Token>/',Chat.as_asgi())

]


