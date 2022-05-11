from django.urls import path
from videojuego.views import *

urlpatterns = [
    path('inicio/', cargar_inicio)
]