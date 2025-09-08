from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    """Login simplificado - entra directamente sin validaciones"""
    if request.method == 'POST':
        # Crear o obtener un usuario por defecto para demo
        user, created = User.objects.get_or_create(
            username='demo_user',
            defaults={
                'email': 'demo@example.com',
                'first_name': 'Usuario',
                'last_name': 'Demo'
            }
        )
        
        # Hacer login automático
        login(request, user)
        return redirect('dashboard')
    
    return render(request, 'usuarios/login.html')

def register_view(request):
    """Registro simplificado - crea usuario directamente"""
    if request.method == 'POST':
        # Obtener datos básicos del formulario (opcional)
        company_name = request.POST.get('company_name', 'Empresa Demo')
        email = request.POST.get('email', f'user{User.objects.count() + 1}@demo.com')
        
        # Crear usuario sin validaciones
        user, created = User.objects.get_or_create(
            username=email,
            defaults={
                'email': email,
                'first_name': company_name,
                'last_name': 'Usuario'
            }
        )
        
        # Login automático después del registro
        login(request, user)
        messages.success(request, 'Registro exitoso. Bienvenido!')
        return redirect('dashboard')
    
    return render(request, 'usuarios/register.html')

def password_reset_view(request):
    """Vista de reset de password - solo muestra mensaje demo"""
    if request.method == 'POST':
        messages.info(request, 'Función de reset deshabilitada en versión demo')
        return redirect('login')
    
    return render(request, 'usuarios/password_reset.html', {
        'demo_mode': True,
        'message': 'Función deshabilitada en versión demo'
    })

def verify_code_view(request):
    """Vista de verificación - solo muestra mensaje demo"""
    if request.method == 'POST':
        messages.info(request, 'Función de verificación deshabilitada en versión demo')
        return redirect('login')
    
    return render(request, 'usuarios/verify_code.html', {
        'demo_mode': True,
        'message': 'Función deshabilitada en versión demo'
    })

def resend_code_view(request):
    """Vista para reenviar código - deshabilitada en demo"""
    messages.info(request, 'Función deshabilitada en versión demo')
    return redirect('login')

def reset_password_confirm(request, token=None):
    """Vista de confirmación - deshabilitada en demo"""
    messages.info(request, 'Función deshabilitada en versión demo')
    return redirect('login')

def logout_view(request):
    """Logout simple"""
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente')
    return redirect('login')