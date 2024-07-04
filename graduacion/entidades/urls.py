from django.urls import path, include
from entidades.views import *

urlpatterns = [
    path('', home, name="home"),
    path('maestrias/', maestrias, name="maestrias"),
    path('alumno/', alumno, name="alumno"),
    path('trabajodegrado/', trabajodegrado, name="trabajodegrado"),
    path('sustentacion/', sustentacion, name="sustentacion"),

#Formularios
path('maestriasForm/', maestriasForm, name="maestriasForm"),

#Buscar
path('buscarMaestrias/', buscarMaestrias, name="buscarMaestrias"),
path('buscarMaestrias/', encontrarMaestrias, name="encontrarMaestrias"),
]   