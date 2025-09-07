from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from dispositivos.models import Organization, PasswordResetToken
import random
import string

def generate_reset_code():
    """Genera un código de 6 dígitos aleatorio"""
    return ''.join(random.choices(string.digits, k=6))

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Credenciales inválidas')
    
    return render(request, 'usuarios/login.html')

def register_view(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        
        if password != password_confirm:
            messages.error(request, 'Las contraseñas no coinciden')
        elif User.objects.filter(username=email).exists():
            messages.error(request, 'El correo ya está registrado')
        else:
            # Crear usuario
            user = User.objects.create_user(
                username=email, 
                email=email, 
                password=password,
                first_name=company_name
            )
            
            # Crear organización
            Organization.objects.create(name=company_name, email=email)
            
            messages.success(request, 'Registro exitoso. Puedes iniciar sesión.')
            return redirect('login')
    
    return render(request, 'usuarios/register.html')

def password_reset_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            # FIX: Usar filter().first() para evitar MultipleObjectsReturned
            user = User.objects.filter(email=email).first()
            
            if not user:
                raise User.DoesNotExist("No user found with this email")
            
            # Generar código de 6 dígitos
            code = generate_reset_code()
            token = PasswordResetToken.objects.create(user=user, code=code)
            
            # Enviar email con código
            try:
                # FIX: Email simplificado para evitar problemas de codificación
                email_subject = 'Codigo de recuperacion - EcoEnergy'
                email_body = f'Tu codigo de recuperacion es: {code}\n\nEste codigo expira en 10 minutos.\n\nSaludos,\nEquipo EcoEnergy'
                
                send_mail(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False
                )
                # Redirigir a página de verificación de código
                return render(request, 'usuarios/verify_code.html', {'email': email})
            except Exception as e:
                messages.error(request, f'Error al enviar el correo: {str(e)}')
        except User.DoesNotExist:
            messages.error(request, 'No existe una cuenta con ese correo electrónico')
        except Exception as e:
            messages.error(request, f'Error inesperado: {str(e)}')
    
    return render(request, 'usuarios/password_reset.html')

def verify_code_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        
        # PROBLEMA 1: El código debe venir de los 6 inputs individuales
        # Tu template HTML usa inputs separados, pero tu vista busca 'code'
        code_digits = []
        for i in range(6):
            digit = request.POST.get(f'code_digit_{i}', '').strip()
            if digit:
                code_digits.append(digit)
        
        # Si no hay dígitos individuales, intentar con el campo 'code' (fallback)
        if not code_digits:
            code = request.POST.get('code', '').strip()
        else:
            code = ''.join(code_digits)
        
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        print(f"DEBUG: email={email}, code='{code}', password={bool(password)}")  # Para debugging
        
        # PROBLEMA 2: Validar que el código tenga exactamente 6 dígitos
        if not code or len(code) != 6 or not code.isdigit():
            messages.error(request, 'Por favor ingresa un código de 6 dígitos válido')
            return render(request, 'usuarios/verify_code.html', {'email': email})
        
        try:
            user = User.objects.filter(email=email).first()
            if not user:
                messages.error(request, 'Usuario no encontrado')
                return render(request, 'usuarios/verify_code.html', {'email': email})
                
            # PROBLEMA 3: Buscar token válido y no usado
            token = PasswordResetToken.objects.filter(
                user=user, 
                code=code, 
                used=False
            ).first()
            
            if not token:
                messages.error(request, 'Código inválido o ya utilizado')
                return render(request, 'usuarios/verify_code.html', {'email': email})
            
            if not token.is_valid():
                messages.error(request, 'El código ha expirado. Solicita uno nuevo.')
                return redirect('password_reset')
            
            # PASO 1: Si solo se envió el código (sin contraseñas), verificarlo
            if not password and not password_confirm:
                messages.success(request, '¡Código verificado correctamente! Ahora ingresa tu nueva contraseña.')
                return render(request, 'usuarios/verify_code.html', {
                    'email': email, 
                    'code_verified': True,
                    'code': code
                })
            
            # PASO 2: Si se enviaron las contraseñas, procesarlas
            if password and password_confirm:
                if password != password_confirm:
                    messages.error(request, 'Las contraseñas no coinciden')
                    return render(request, 'usuarios/verify_code.html', {
                        'email': email, 
                        'code_verified': True,
                        'code': code
                    })
                
                if len(password) < 6:
                    messages.error(request, 'La contraseña debe tener al menos 6 caracteres')
                    return render(request, 'usuarios/verify_code.html', {
                        'email': email, 
                        'code_verified': True,
                        'code': code
                    })
                
                # Cambiar contraseña
                user.set_password(password)
                user.save()
                
                # Marcar token como usado
                token.used = True
                token.save()
                
                # PROBLEMA 4: Limpiar todos los tokens del usuario
                PasswordResetToken.objects.filter(user=user).update(used=True)
                
                messages.success(request, 'Contraseña cambiada exitosamente. Puedes iniciar sesión.')
                return redirect('login')
                
        except Exception as e:
            print(f"ERROR en verify_code_view: {str(e)}")  # Para debugging
            messages.error(request, 'Error interno. Inténtalo de nuevo.')
            return render(request, 'usuarios/verify_code.html', {'email': email})
    
    # GET request
    email = request.GET.get('email', '')
    return render(request, 'usuarios/verify_code.html', {'email': email})

def resend_code_view(request):
    """Vista para reenviar código de verificación"""
    if request.method == 'POST':
        email = request.POST['email']
        try:
            # FIX: Usar filter().first() para evitar MultipleObjectsReturned
            user = User.objects.filter(email=email).first()
            if not user:
                raise User.DoesNotExist("No user found")
            
            # Marcar tokens anteriores como usados
            PasswordResetToken.objects.filter(user=user, used=False).update(used=True)
            
            # Generar nuevo código
            code = generate_reset_code()
            token = PasswordResetToken.objects.create(user=user, code=code)
            
            # Reenviar email
            try:
                # FIX: Email simplificado para evitar problemas de codificación
                email_subject = 'Nuevo codigo de recuperacion - EcoEnergy'
                email_body = f'Tu nuevo codigo de recuperacion es: {code}\n\nEste codigo expira en 10 minutos.'
                
                send_mail(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False
                )
                messages.success(request, 'Se ha enviado un nuevo código a tu correo')
                return render(request, 'usuarios/verify_code.html', {'email': email})
            except Exception as e:
                messages.error(request, f'Error al reenviar el código: {str(e)}')
        except User.DoesNotExist:
            messages.error(request, 'Email no encontrado')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
    
    return redirect('password_reset')

# Vista obsoleta mantenida para compatibilidad (no se usa más)
def reset_password_confirm(request, token):
    messages.info(request, 'Por favor usa el sistema de códigos de verificación.')
    return redirect('password_reset')

def logout_view(request):
    logout(request)
    return redirect('login')