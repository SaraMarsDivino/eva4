#serializers.py api
from rest_framework import serializers
from .models import Clase, Estudiante, Profesor


class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['id', 'nombre', 'horario', 'descripcion']

class EstudianteSerializer(serializers.ModelSerializer):
    clases_inscritas = ClaseSerializer(many=True, read_only=True)
    clases_inscritas_ids = serializers.PrimaryKeyRelatedField(
        queryset=Clase.objects.all(), many=True, write_only=True, source='clases_inscritas'
    )

    class Meta:
        model = Estudiante
        fields = ['id', 'nombre', 'correo', 'clases_inscritas', 'clases_inscritas_ids']

    def update(self, instance, validated_data):
        clases_ids = validated_data.pop('clases_inscritas', None)
        instance = super().update(instance, validated_data)

        if clases_ids is not None:
            instance.clases_inscritas.set(clases_ids)  # Sobrescribe las clases inscritas

        return instance



# Serializador para el modelo Profesor
class ProfesorSerializer(serializers.ModelSerializer):
    clases_impartidas = serializers.SerializerMethodField()

    class Meta:
        model = Profesor
        fields = ['id', 'nombre', 'especialidad', 'clases_impartidas']

    def get_clases_impartidas(self, obj):
        return [clase.nombre for clase in obj.clases_impartidas.all()]
