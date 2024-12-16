from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Clase, Estudiante, Profesor
from .serializers import ClaseSerializer, EstudianteSerializer, ProfesorSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login


# CRUD para Clases
class ClaseViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer
    permission_classes = [IsAuthenticated]


# CRUD para Estudiantes
class EstudianteViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        clases_ids = request.data.get('clases_inscritas', [])
        self._validar_clases(clases_ids)
        estudiante = super().create(request, *args, **kwargs)
        estudiante.instance.clases_inscritas.set(clases_ids)
        return estudiante

    def update(self, request, *args, **kwargs):
        clases_ids = request.data.get('clases_inscritas', [])
        self._validar_clases(clases_ids)
        estudiante = self.get_object()
        response = super().update(request, *args, **kwargs)
        estudiante.clases_inscritas.set(clases_ids)  # Actualiza las clases inscritas
        return response

    def _validar_clases(self, clases_ids):
        """
        Valida que las clases proporcionadas existan en la base de datos.
        """
        if not all(Clase.objects.filter(id=clase_id).exists() for clase_id in clases_ids):
            raise ValidationError({"detail": "Algunas clases proporcionadas no existen."})


# CRUD para Profesores
class ProfesorViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Valida y asigna las clases impartidas al crear un profesor.
        """
        clases_ids = self.request.data.get('clases_impartidas', [])
        self._validar_clases(clases_ids)
        profesor = serializer.save()
        profesor.clases_impartidas.set(clases_ids)

    def perform_update(self, serializer):
        """
        Valida y actualiza las clases impartidas al editar un profesor.
        """
        clases_ids = self.request.data.get('clases_impartidas', [])
        self._validar_clases(clases_ids)
        profesor = serializer.save()
        profesor.clases_impartidas.set(clases_ids)

    def _validar_clases(self, clases_ids):
        """
        Valida que las clases proporcionadas existan en la base de datos.
        """
        if not all(Clase.objects.filter(id=clase_id).exists() for clase_id in clases_ids):
            raise ValidationError({"detail": "Algunas clases proporcionadas no existen."})


# Búsquedas personalizadas: Clases por profesor o horario
class BuscarClasesView(LoginRequiredMixin, APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profesor = request.query_params.get('profesor')
        horario = request.query_params.get('horario')

        if not profesor and not horario:
            return Response(
                {"detail": "Debe proporcionar al menos un parámetro (profesor o horario)."},
                status=status.HTTP_400_BAD_REQUEST
            )

        clases = Clase.objects.all()
        if profesor:
            clases = clases.filter(profesores__nombre__icontains=profesor)
        if horario:
            clases = clases.filter(horario=horario)

        serializer = ClaseSerializer(clases, many=True)
        return Response(serializer.data)



@login_required
def menu_principal(request):
    return render(request, 'menu.html')






def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('menu')  # Redirige al menú principal
        else:
            return render(request, 'login/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'login/login.html')

