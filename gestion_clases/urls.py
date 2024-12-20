"""
URL configuration for gestion_clases project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py principal del proyecto
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # API URLs
    path('api/', include('api.urls')),

    # Rutas de Login y Logout
    path('', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Menú principal (requiere autenticación)
    path('menu/', login_required(TemplateView.as_view(template_name="menu.html")), name="menu"),

    # Vistas protegidas específicas de cada funcionalidad
    path('clases/', login_required(TemplateView.as_view(template_name="clases/list.html")), name="clases"),
    path('estudiantes/', login_required(TemplateView.as_view(template_name="estudiantes/list.html")), name="estudiantes"),
    path('profesores/', login_required(TemplateView.as_view(template_name="profesores/list.html")), name="profesores"),
]
