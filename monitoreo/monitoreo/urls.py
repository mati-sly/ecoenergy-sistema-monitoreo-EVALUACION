"""
URL configuration for monitoreo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from dispositivos.views import (
    # Vistas principales requeridas por la evaluación
    dashboard, device_list, device_detail, measurement_list, alert_summary,
    # Vistas CRUD
    crear_dispositivo, editar_dispositivo, eliminar_dispositivo,
    # Vistas originales para compatibilidad
    inicio, dispositivo, panel_dispositivos
)

# Importaciones simplificadas para versión demo
from usuarios.views import login_view, register_view, password_reset_view, logout_view, verify_code_view, reset_password_confirm

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # RUTAS DE AUTENTICACIÓN SIMPLIFICADAS:
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('password-reset/', password_reset_view, name='password_reset'),
    path('verify-code/', verify_code_view, name='verify_code'),
    path('logout/', logout_view, name='logout'),
    
    # Ruta obsoleta comentada - función no disponible en versión demo
    # path('reset-password/<uuid:token>/', reset_password_confirm, name='reset_password_confirm'),
    
    # Rutas principales para la evaluación
    path('', dashboard, name='dashboard'),  # HU1 - Dashboard
    path('devices/', device_list, name='device_list'),  # HU2 - Lista con filtro
    path('devices/<int:device_id>/', device_detail, name='device_detail'),  # HU3 - Detalle
    path('measurements/', measurement_list, name='measurement_list'),  # HU4 - Lista mediciones
    path('alerts/', alert_summary, name='alert_summary'),  # HU5 - Resumen alertas
    
    # Rutas CRUD
    path('devices/create/', crear_dispositivo, name='crear_dispositivo'),
    path('devices/<int:dispositivo_id>/edit/', editar_dispositivo, name='editar_dispositivo'),
    path('devices/<int:dispositivo_id>/delete/', eliminar_dispositivo, name='eliminar_dispositivo'),
    
    # Rutas originales para compatibilidad
    path('inicio/', inicio, name='inicio'),
    path('dispositivos/', inicio, name='dispositivos'),
    path('dispositivos/<int:dispositivo_id>/', dispositivo, name='dispositivo'),
    path('panel/', panel_dispositivos, name='panel'),
]