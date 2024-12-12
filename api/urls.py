from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClaseViewSet, EstudianteViewSet, ProfesorViewSet, ClaseSearchView, BuscarClasesView

# Router para las vistas basadas en modelos (CRUD)
router = DefaultRouter()
router.register('clases', ClaseViewSet, basename='clase')
router.register('estudiantes', EstudianteViewSet, basename='estudiante')
router.register('profesores', ProfesorViewSet, basename='profesor')

# Rutas de la API
urlpatterns = [
    # Rutas generadas automáticamente por el router
    path('', include(router.urls)),

    # Ruta para búsqueda personalizada
    path('clases/buscar/', BuscarClasesView.as_view(), name='buscar-clases'),

    # Ruta para autenticación por token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
