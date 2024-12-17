# urls.py de api
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClaseViewSet, EstudianteViewSet, ProfesorViewSet, BuscarClasesView
from rest_framework.authtoken.views import obtain_auth_token
from .views import ClaseViewSet, EstudianteViewSet, ProfesorViewSet

router = DefaultRouter()
router.register('clases', ClaseViewSet)
router.register('estudiantes', EstudianteViewSet)
router.register('profesores', ProfesorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns = [
    # Rutas CRUD generadas por DRF
    path('', include(router.urls)),

    # Ruta para búsqueda personalizada de clases
    path('clases/buscar/', BuscarClasesView.as_view(), name='buscar_clases'),

    # Autenticación por token para DRF
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
