from rest_framework import serializers
from .models import Clase, Estudiante, Profesor

# Serializador de Clase
class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['id', 'nombre', 'horario', 'descripcion']

# Serializador de Estudiante
class EstudianteSerializer(serializers.ModelSerializer):
    clases_inscritas = serializers.PrimaryKeyRelatedField(
        queryset=Clase.objects.all(), many=True, required=False
    )

    class Meta:
        model = Estudiante
        fields = ['id', 'nombre', 'correo', 'clases_inscritas']

    def update(self, instance, validated_data):
        clases_ids = validated_data.pop('clases_inscritas', None)
        if clases_ids is not None:
            instance.clases_inscritas.set(clases_ids)
        return super().update(instance, validated_data)


# Serializador de Profesor
class ProfesorSerializer(serializers.ModelSerializer):
    clases_impartidas = serializers.PrimaryKeyRelatedField(
        queryset=Clase.objects.all(), many=True, required=False
    )

    class Meta:
        model = Profesor
        fields = ['id', 'nombre', 'especialidad', 'clases_impartidas']
