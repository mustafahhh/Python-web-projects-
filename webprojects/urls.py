from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('make/',views.make,name='make'),
    path('pulldata/',views.datapull,name='datapull'),
    path('date/',views.date,name='date')
]
