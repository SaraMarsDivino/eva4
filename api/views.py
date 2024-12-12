from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Clase, Estudiante, Profesor
from .serializers import ClaseSerializer, EstudianteSerializer, ProfesorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# CRUD para Clases
class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer
    permission_classes = [IsAuthenticated]

# CRUD para Estudiantes
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = [IsAuthenticated]

# CRUD para Profesores
class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    permission_classes = [IsAuthenticated]

# Búsquedas personalizadas: Clases por profesor o horario
class BuscarClasesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profesor = request.query_params.get('profesor')
        horario = request.query_params.get('horario')

        # Filtrar clases dinámicamente según los parámetros proporcionados
        clases = Clase.objects.all()
        if profesor:
            clases = clases.filter(profesores__nombre__icontains=profesor)
        if horario:
            clases = clases.filter(horario=horario)

        serializer = ClaseSerializer(clases, many=True)
        return Response(serializer.data)
