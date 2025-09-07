# 🌱 EcoEnergy - Sistema de Monitoreo Energético

Sistema web de monitoreo energético desarrollado en Django para evaluación académica. Permite a las empresas gestionar dispositivos IoT, monitorear consumo energético y recibir alertas en tiempo real.

## 📋 Características Principales

### ✅ Funcionalidades Implementadas

#### 📊 **Dashboard Principal (HU1)**

- Contadores por categoría y zona
- Resumen de alertas por severidad
- Últimas mediciones registradas
- Interfaz con diseño Frutiger Aero (gradientes celeste-verde)

#### 🔧 **Gestión de Dispositivos (HU2-HU3)**

- Lista de dispositivos con filtro por categoría
- Detalle completo de cada dispositivo
- Visualización de mediciones y alertas asociadas
- Estados de funcionamiento en tiempo real

#### 📈 **Historial de Mediciones (HU4)**

- Lista completa de mediciones históricas
- Filtros por fecha y dispositivo
- Valores de consumo energético detallados

#### 🚨 **Sistema de Alertas (HU5)**

- Resumen de alertas por severidad
- Alertas de la semana actual
- Clasificación por niveles (Info, Warning, Critical)

#### 🔐 **Sistema de Autenticación (HU6-HU8)**

- Login de usuarios
- Registro de empresas con verificación por email
- Recuperación de contraseña con códigos de verificación
- Protección de vistas con autenticación requerida

## 🏗️ Arquitectura del Proyecto

### 📁 Estructura de Directorios

```
monitoreo/
├── db.sqlite3                      # Base de datos SQLite
├── manage.py                       # Script de gestión Django
├── monitoreo/                      # Configuración principal
│   ├── settings.py                 # Configuraciones
│   ├── urls.py                     # URLs principales
│   └── wsgi.py                     # WSGI config
├── dispositivos/                   # App principal - modelos de negocio
│   ├── models.py                   # Organization, Device, Measurement, Alert
│   ├── views.py                    # Vistas del dashboard y dispositivos
│   ├── forms.py                    # Formularios
│   ├── admin.py                    # Panel de administración
│   └── templates/dispositivos/     # Templates principales
│       ├── dashboard.html          # Dashboard principal
│       ├── device_list.html        # Lista de dispositivos
│       ├── device_detail.html      # Detalle de dispositivo
│       ├── measurement_list.html   # Historial de mediciones
│       └── alert_summary.html      # Resumen de alertas
└── usuarios/                       # App de autenticación
    ├── models.py                   # VerificationCode, UserProfile
    ├── views.py                    # Login, registro, recuperación
    └── templates/usuarios/         # Templates de auth
        ├── login.html              # Inicio de sesión
        ├── register.html           # Registro de empresas
        ├── password_reset.html     # Solicitar recuperación
        └── verify_code.html        # Verificar código email
```

### 🗄️ Modelos de Datos

#### **dispositivos/models.py**

- `Organization`: Empresas registradas
- `Category`: Categorías de dispositivos (HVAC, Lighting, etc.)
- `Zone`: Zonas físicas (Office, Warehouse, etc.)
- `Device`: Dispositivos IoT de monitoreo
- `Measurement`: Mediciones de consumo energético
- `Alert`: Alertas del sistema
- `PasswordResetToken`: Tokens para recuperación de contraseña

#### **usuarios/models.py**

- `VerificationCode`: Códigos de verificación por email
- `UserProfile`: Perfiles extendidos de usuario

## 🎨 Diseño Visual

### **Estilo Frutiger Aero**

- **Colores principales**: Gradientes celeste (#87CEEB) a verde (#98FB98)
- **Efectos visuales**:
  - Backdrop blur y transparencias
  - Sombras suaves
  - Transiciones fluidas
  - Elementos flotantes animados
- **Tipografía**: Segoe UI para legibilidad moderna
- **Iconografía**: Emojis y símbolos relacionados con energía/ecología

## 🔧 Configuración y Uso

### **Prerrequisitos**

```bash
Python 3.8+
Django 4.2+
```

### **Instalación**

```bash
# Clonar el proyecto
git clone [repositorio]
cd monitoreo

# Instalar dependencias
pip install django

# Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

### **Configuración de Email**

Para que funcione la verificación por email, configura en `settings.py`:

```python
# Email configuration para Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'tu-app-password'  # App password de Gmail
DEFAULT_FROM_EMAIL = 'tu-email@gmail.com'
```

### **URLs Disponibles**

```
/                    → Dashboard principal
/devices/            → Lista de dispositivos
/devices/<id>/       → Detalle de dispositivo
/measurements/       → Historial de mediciones
/alerts/             → Resumen de alertas
/login/              → Inicio de sesión
/register/           → Registro de empresas
/password-reset/     → Recuperación de contraseña
/admin/              → Panel de administración
```

## 📊 Datos de Ejemplo

El sistema incluye datos precargados para testing:

### **Organizaciones**

- Green Solutions Ltd.
- EcoTech Industries
- Sustainable Corp

### **Categorías de Dispositivos**

- HVAC (Climatización)
- Lighting (Iluminación)
- Appliances (Electrodomésticos)
- Security (Seguridad)

### **Zonas**

- Office (Oficina)
- Warehouse (Almacén)
- Production (Producción)
- Parking (Estacionamiento)

### **Dispositivos Ejemplo**

- Smart Thermostat (HVAC)
- LED Panel Controller (Lighting)
- Industrial Refrigerator (Appliances)
- Security Camera System (Security)

## 🐛 Problemas Conocidos y Soluciones

### **Problema: Error CSRF 403**

**Causa**: Falta el token CSRF en formularios
**Solución**: Verificar que todos los templates tengan `{% csrf_token %}`

### **Problema: Código de verificación se reenvía**

**Causa**: JavaScript no envía correctamente el código de 6 dígitos
**Solución**: Verificar que el campo oculto `hiddenCode` se actualice correctamente

### **Problema: Usuario no se autentica**

**Causa**: Usuario creado como `is_active=False`
**Solución**: Activar usuario después de verificar email

## 🔄 Estado del Desarrollo

### ✅ **Completado**

- [x] Modelos de datos con relaciones
- [x] Dashboard con métricas
- [x] CRUD de dispositivos
- [x] Lista de mediciones
- [x] Sistema de alertas
- [x] Templates con diseño Frutiger Aero
- [x] Panel de administración
- [x] Datos de ejemplo

### 🔄 **En Progreso**

- [ ] Sistema de autenticación (99% - debugging final)
- [ ] Validación de códigos de verificación
- [ ] Protección de vistas con `@login_required`

### 📋 **Por Implementar**

- [ ] Tests unitarios
- [ ] API REST endpoints
- [ ] Gráficos interactivos de consumo
- [ ] Notificaciones push
- [ ] Exportación de reportes
- [ ] Dashboard responsive móvil

## 👥 Roles de Usuario

### **Administrador**

- Acceso completo al panel Django admin
- Gestión de organizaciones y usuarios
- Configuración del sistema

### **Usuario Empresa**

- Acceso a dashboard de su organización
- Gestión de dispositivos propios
- Visualización de mediciones y alertas
- Generación de reportes

## 📧 Configuración de Verificación por Email

### **Para Gmail (Recomendado para desarrollo)**

1. Activar verificación en 2 pasos en tu cuenta Google
2. Generar "Contraseña de aplicación" específica
3. Usar esa contraseña en `EMAIL_HOST_PASSWORD`
4. Configurar `EMAIL_HOST_USER` con tu email de Gmail

### **Para Producción**

- Usar servicios como SendGrid, Mailgun o Amazon SES
- Configurar dominio propio para emails
- Implementar templates HTML para emails

## 🚀 Historias de Usuario Implementadas

- **HU1**: Dashboard con métricas principales ✅
- **HU2**: Lista de dispositivos con filtros ✅
- **HU3**: Detalle completo de dispositivos ✅
- **HU4**: Historial de mediciones ✅
- **HU5**: Resumen de alertas por severidad ✅
- **HU6**: Login funcional ✅
- **HU7**: Registro de empresas 🔄
- **HU8**: Recuperación de contraseña 🔄

## 📝 Notas de Desarrollo

### **Consideraciones Técnicas**

- Base de datos SQLite para desarrollo (cambiar a PostgreSQL en producción)
- Campos `created_at`, `updated_at`, `deleted_at` en todos los modelos
- Soft deletes implementados donde corresponde
- Relaciones FK correctas entre modelos

### **Estilo y UX**

- Diseño Frutiger Aero consistente en todas las páginas
- Responsive design con breakpoints móviles
- Animaciones CSS para mejor experiencia
- Feedback visual para todas las acciones del usuario

### **Seguridad**

- Protección CSRF en todos los formularios
- Validación de entrada en backend
- Expiración de códigos de verificación (10 minutos)
- Contraseñas hasheadas con Django auth

## 🤝 Contribución

Este es un proyecto académico para evaluación. Para modificaciones:

1. Fork del repositorio
2. Crear rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## 📄 Licencia

Proyecto académico - Solo para fines educativos

## 👨‍💻 Autor

Desarrollado como parte de evaluación académica para el curso de Backend

---

**Última actualización**: Septiembre 2025  
**Versión**: 1.0.0-beta  
**Estado**: En desarrollo activo
