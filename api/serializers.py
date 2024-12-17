#serializers.py api
from rest_framework import serializers
from .models import Clase, Estudiante, Profesor


class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['id', 'nombre', 'horario', 'descripcion']  # Listar explícitamente los campos


# Serializador para el modelo Estudiante
class EstudianteSerializer(serializers.ModelSerializer):
    clases_inscritas = serializers.SerializerMethodField()

    class Meta:
        model = Estudiante
        fields = ['id', 'nombre', 'correo', 'clases_inscritas']

    def get_clases_inscritas(self, obj):
        # Devuelve los nombres de las clases inscritas
        return [clase.nombre for clase in obj.clases_inscritas.all()]

    def update(self, instance, validated_data):
        clases_ids = self.initial_data.get('clases_inscritas', [])
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.correo = validated_data.get('correo', instance.correo)

        if clases_ids:
            instance.clases_inscritas.set(Clase.objects.filter(id__in=clases_ids))

        instance.save()
        return instance


# Serializador para el modelo Profesor
class ProfesorSerializer(serializers.ModelSerializer):
    clases_impartidas = serializers.SerializerMethodField()

    class Meta:
        model = Profesor
        fields = ['id', 'nombre', 'especialidad', 'clases_impartidas']

    def get_clases_impartidas(self, obj):
        return [clase.nombre for clase in obj.clases_impartidas.all()]
