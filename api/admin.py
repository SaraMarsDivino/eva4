from django.contrib import admin
from .models import Clase, Estudiante, Profesor

# Registro de modelos en el panel de administración
@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'horario', 'descripcion')
    search_fields = ('nombre', 'horario')
    list_filter = ('horario',)

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo')
    search_fields = ('nombre', 'correo')
    filter_horizontal = ('clases_inscritas',)

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'especialidad')
    search_fields = ('nombre', 'especialidad')
    filter_horizontal = ('clases_impartidas',)
