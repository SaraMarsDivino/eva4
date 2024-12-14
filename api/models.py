from django.db import models

# Modelo Clase
class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    horario = models.TimeField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


# Modelo Estudiante
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    clases_inscritas = models.ManyToManyField(Clase, related_name="estudiantes", blank=True)

    def __str__(self):
        return self.nombre


# Modelo Profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    clases_impartidas = models.ManyToManyField(Clase, related_name="profesores", blank=True)

    def __str__(self):
        return self.nombre
