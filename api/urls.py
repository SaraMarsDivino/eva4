#urls.py de api
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import menu_principal, ClaseViewSet, EstudianteViewSet, ProfesorViewSet, BuscarClasesView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Router para CRUD
router = DefaultRouter()
router.register('clases', ClaseViewSet, basename='clase')
router.register('estudiantes', EstudianteViewSet, basename='estudiante')
router.register('profesores', ProfesorViewSet, basename='profesor')

urlpatterns = [
    # Rutas para el CRUD generado por DRF
    path('', include(router.urls)),

    # Rutas de autenticación
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('menu/', menu_principal, name='menu'),

    # Ruta de búsqueda personalizada
    path('clases/buscar/', BuscarClasesView.as_view(), name='buscar_clases'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

