from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClaseViewSet, EstudianteViewSet, ProfesorViewSet, BuscarClasesView
from rest_framework.authtoken.views import obtain_auth_token

# Router para vistas CRUD
router = DefaultRouter()
router.register('clases', ClaseViewSet, basename='clase')
router.register('estudiantes', EstudianteViewSet, basename='estudiante')
router.register('profesores', ProfesorViewSet, basename='profesor')

urlpatterns = [
    path('', include(router.urls)),
    path('clases/buscar/', BuscarClasesView.as_view(), name='buscar_clases'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
