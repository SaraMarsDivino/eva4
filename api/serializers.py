from rest_framework import serializers
from .models import Clase, Estudiante, Profesor

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

class ProfesorSerializer(serializers.ModelSerializer):
    clases_impartidas = ClaseSerializer(many=True, read_only=True)

    class Meta:
        model = Profesor
        fields = '__all__'
    
