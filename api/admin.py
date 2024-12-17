from django.contrib import admin
from .models import Profesor, Clase, Estudiante

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especialidad']
    filter_horizontal = ['clases_impartidas']  # Ahora es válido porque Clase está definida antes

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'horario', 'descripcion']

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'correo']
    filter_horizontal = ['clases_inscritas']
