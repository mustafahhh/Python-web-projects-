from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
import os 



url_patterns = [ 
    path('',views.login),
    path('makeroom/',views.makeroom),
    path('joinroom/',views.joinroom),
    path('chatroom/<str:ID>/',views.chatroom),    
    path('middle/',views.middlewebpage)
]
api_urls = [
    path('checkroom/<str:room>/',views.roomcheckApi),
    path('makeroom/',views.makeroomApi),
    path('makeuser/<str:User>/',views.makeAccountApi),
]

if settings.DEBUG:
    url_patterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



#1:26