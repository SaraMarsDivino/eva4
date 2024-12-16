#serializers.py api
from rest_framework import serializers
from .models import Clase, Estudiante, Profesor


class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['id', 'nombre', 'horario', 'descripcion']  # Listar explícitamente los campos



class EstudianteSerializer(serializers.ModelSerializer):
    clases_inscritas = serializers.PrimaryKeyRelatedField(
        queryset=Clase.objects.all(), many=True, required=False
    )

    class Meta:
        model = Estudiante
        fields = ['id', 'nombre', 'correo', 'clases_inscritas']

    def update(self, instance, validated_data):
        clases_ids = validated_data.pop('clases_inscritas', None)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.correo = validated_data.get('correo', instance.correo)

        if clases_ids is not None:
            instance.clases_inscritas.set(clases_ids)

        instance.save()
        return instance





class ProfesorSerializer(serializers.ModelSerializer):
    clases_impartidas = serializers.PrimaryKeyRelatedField(
        queryset=Clase.objects.all(), many=True, required=False
    )

    class Meta:
        model = Profesor
        fields = ['id', 'nombre', 'especialidad', 'clases_impartidas']

    def update(self, instance, validated_data):
        """
        Permite actualizar el profesor y sus clases impartidas.
        """
        clases_ids = validated_data.pop('clases_impartidas', None)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.especialidad = validated_data.get('especialidad', instance.especialidad)

        if clases_ids is not None:
            instance.clases_impartidas.set(clases_ids)

        instance.save()
        return instance