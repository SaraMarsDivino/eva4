from django.db import models
from django.contrib.auth.models import User

class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    horario = models.TimeField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    clases_inscritas = models.ManyToManyField(Clase, related_name="estudiantes")

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(null=False, max_length=100)
    especialidad = models.CharField(max_length=100)
    clases_impartidas = models.ManyToManyField(Clase, related_name="profesores")

    def __str__(self):
        return self.nombre
