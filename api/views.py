from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from .models import Clase, Estudiante, Profesor
from .serializers import ClaseSerializer, EstudianteSerializer, ProfesorSerializer
from rest_framework.views import APIView

# Configuración de Paginación Global
class DefaultPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

# CRUD para Clases
class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagination

# Configuración de paginación
class DefaultPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

# CRUD para Estudiantes
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagination

    def update(self, request, *args, **kwargs):
        estudiante = self.get_object()
        clases_ids = request.data.get('clases_inscritas', [])

        # Validar que se proporcionaron IDs de clases
        if not clases_ids:
            raise ValidationError({"detail": "Debe proporcionar al menos una clase para inscribir al estudiante."})

        # Validar que todas las clases existen
        clases_validas = Clase.objects.filter(id__in=clases_ids)
        if clases_validas.count() != len(clases_ids):
            raise ValidationError({"detail": "Algunas clases proporcionadas no existen."})

        # Actualizar las clases inscritas del estudiante
        estudiante.clases_inscritas.set(clases_validas)
        estudiante.save()

        # Retornar la respuesta con el serializador actualizado
        return Response(self.serializer_class(estudiante).data, status=status.HTTP_200_OK)

# CRUD para Profesores

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagination

    def perform_create(self, serializer):
        clases_ids = self.request.data.get('clases_impartidas', [])
        profesor = serializer.save()
        if clases_ids:
            profesor.clases_impartidas.set(clases_ids)

    def perform_update(self, serializer):
        clases_ids = self.request.data.get('clases_impartidas', [])
        profesor = serializer.save()
        if clases_ids:
            profesor.clases_impartidas.set(clases_ids)


# Búsqueda de Clases
class BuscarClasesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profesor = request.query_params.get('profesor')
        horario = request.query_params.get('horario')

        if not profesor and not horario:
            return Response(
                {"detail": "Debe proporcionar al menos un parámetro (profesor o horario)."},
                status=400
            )

        clases = Clase.objects.all()
        if profesor:
            clases = clases.filter(profesor__nombre__icontains=profesor)
        if horario:
            clases = clases.filter(horario=horario)

        serializer = ClaseSerializer(clases, many=True)
        return Response(serializer.data)
