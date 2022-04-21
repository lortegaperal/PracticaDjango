from django.db import models


class Compañia(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=150)
    independiente = models.BooleanField


class Videojuego(models.Model):

    id = models.IntegerField(primary_key= True)
    nombre = models.TextField(max_length=150)
    num_horas = models.IntegerField()
    genero = models.TextField(max_length=150)
    fecha_publicacion = models.DateTimeField()
    compañia = models.ForeignKey(Compañia, on_delete=models.CASCADE, default=None)


