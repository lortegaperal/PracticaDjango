from django.urls import path
from videojuegos.views import *

urlpatterns = [
    path('inicio/', cargar_inicio)
]