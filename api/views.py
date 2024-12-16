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
        if not self.validar_clases(clases_ids):
            raise ValidationError({"detail": "Algunas clases proporcionadas no existen."})
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        clases_ids = request.data.get('clases_inscritas', [])
        if not self.validar_clases(clases_ids):
            raise ValidationError({"detail": "Algunas clases proporcionadas no existen."})
        return super().update(request, *args, **kwargs)

    def validar_clases(self, clases_ids):
        return all(Clase.objects.filter(id=clase_id).exists() for clase_id in clases_ids)


# CRUD para Profesores
class ProfesorViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        clases_ids = request.data.get('clases_impartidas', [])
        if not self.validar_clases(clases_ids):
            raise ValidationError({"detail": "Algunas clases proporcionadas no existen."})
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        clases_ids = request.data.get('clases_impartidas', [])
        if not self.validar_clases(clases_ids):
            raise ValidationError({"detail": "Algunas clases proporcionadas no existen."})
        return super().update(request, *args, **kwargs)

    def validar_clases(self, clases_ids):
        return all(Clase.objects.filter(id=clase_id).exists() for clase_id in clases_ids)


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



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

# Vista del login
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

