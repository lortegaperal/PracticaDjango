from django.shortcuts import render


def cargar_inicio(request):
    return render(request, "inicio.html")

