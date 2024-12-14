from rest_framework import serializers
from .models import Clase, Estudiante, Profesor

# Serializador para el modelo Clase
class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['id', 'nombre', 'horario', 'descripcion']  # Listar explícitamente los campos


# Serializador para el modelo Estudiante
class EstudianteSerializer(serializers.ModelSerializer):
    clases_inscritas = ClaseSerializer(many=True, read_only=True)  # Incluir clases inscritas en el serializador

    class Meta:
        model = Estudiante
        fields = ['id', 'nombre', 'correo', 'clases_inscritas']  # Personalizar los campos


# Serializador para el modelo Profesor
class ProfesorSerializer(serializers.ModelSerializer):
    clases_impartidas = ClaseSerializer(many=True, read_only=True)  # Incluir clases impartidas en el serializador

    class Meta:
        model = Profesor
        fields = ['id', 'nombre', 'especialidad', 'clases_impartidas']  # Personalizar los campos
