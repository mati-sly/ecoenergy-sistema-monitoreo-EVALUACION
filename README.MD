# EcoEnergy - Sistema de Monitoreo IoT

Sistema de monitoreo para dispositivos de energía renovable desarrollado con Django. Permite a las empresas gestionar y supervisar el consumo energético de sus dispositivos IoT a través de una interfaz web intuitiva.

## Información del Proyecto

- **Asignatura:** Programación Back End (TI3041)
- **Evaluación:** Sumativa I - Unidad 1
- **Docente:** Javier Ahumada Cortes
- **Institución:** Instituto Profesional AIEP - La Serena

## Desarrolladores

- **Matias** - Templates, autenticación y configuración frontend
- **Alma** - Modelos de datos, vistas backend y lógica de negocio

## Características Principales

### Funcionalidades Core

- Dashboard con métricas de dispositivos y consumo energético
- Gestión completa de dispositivos IoT (CRUD)
- Monitoreo de mediciones en tiempo real
- Sistema de alertas por severidad (Grave, Alta, Media)
- Filtrado de dispositivos por categoría y zona
- Autenticación simplificada para demostración

### Arquitectura

- **Backend:** Django 5.2 con Python 3.11+
- **Base de datos:** SQLite con datos de prueba incluidos
- **Frontend:** HTML5, CSS3 con diseño responsive
- **Autenticación:** Sistema simplificado para evaluación académica

## Instalación y Configuración

### Prerrequisitos

```bash
- Python 3.8 o superior
- pip (gestor de paquetes Python)
- Git
```

### Instalación Rápida

1. **Clonar el repositorio**

```bash
git clone https://github.com/mati-sly/ecoenergy-sistema-monitoreo-EVALUACION.git
cd ecoenergy-sistema-monitoreo-EVALUACION
```

2. **Crear entorno virtual**

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**

```bash
# Copiar template de configuración
cp .env.example .env
# Editar .env si es necesario (opcional para demo)
```

5. **Ejecutar migraciones** (si es necesario)

```bash
cd monitoreo
python manage.py migrate
```

6. **Iniciar servidor**

```bash
python manage.py runserver
```

7. **Acceder al sistema**

- URL: `http://127.0.0.1:8000`
- **Login:** Hacer clic en "Acceder al Dashboard" (sin credenciales)
- **Usuario demo:** Se crea automáticamente

## Estructura del Proyecto

```
ecoenergy-sistema-monitoreo-EVALUACION/
├── monitoreo/                          # Proyecto Django principal
│   ├── dispositivos/                   # App principal de dispositivos
│   │   ├── models.py                   # Modelos: Organization, Device, etc.
│   │   ├── views.py                    # Vistas para HU1-HU5
│   │   ├── templates/dispositivos/     # Templates HTML
│   │   ├── management/commands/        # Comandos personalizados
│   │   │   └── seed_data.py           # Generador de datos de prueba
│   │   └── migrations/                 # Migraciones de base de datos
│   ├── usuarios/                       # App de autenticación
│   │   ├── views.py                    # Login simplificado
│   │   └── templates/usuarios/         # Templates de autenticación
│   ├── monitoreo/                      # Configuración Django
│   │   ├── settings.py                 # Configuración principal
│   │   └── urls.py                     # URLs del proyecto
│   ├── db.sqlite3                      # Base de datos con datos de prueba
│   └── manage.py                       # Comando Django
├── requirements.txt                    # Dependencias Python
├── .env.example                       # Template de configuración
├── .gitignore                         # Archivos excluidos de Git
└── README.md                          # Este archivo
```

## Modelos de Datos

### Entidades Principales

- **Organization:** Empresas que contratan el servicio
- **Category:** Categorías de dispositivos (Solar, Eólico, etc.)
- **Zone:** Zonas físicas donde se ubican dispositivos
- **Device:** Dispositivos IoT de monitoreo
- **Measurement:** Mediciones de consumo energético
- **Alert:** Alertas del sistema por anomalías

### Características Técnicas

- Todos los modelos incluyen campos `created_at`, `updated_at`, `deleted_at`
- Relaciones definidas con `Organization` según requisitos
- Nomenclatura en inglés para tablas y campos
- Soft delete implementado para auditoría

## Historias de Usuario Implementadas

### HU1 - Dashboard Principal

- **URL:** `/`
- **Descripción:** Panel con resúmenes de dispositivos por categoría y zona
- **Datos:** Últimas 10 mediciones, alertas de la semana por severidad

### HU2 - Lista de Dispositivos

- **URL:** `/devices/`
- **Descripción:** Listado completo con filtro por categoría
- **Funcionalidad:** Filtrado dinámico y enlaces a detalle

### HU3 - Detalle de Dispositivo

- **URL:** `/devices/<id>/`
- **Descripción:** Información completa del dispositivo
- **Datos:** Mediciones recientes y alertas asociadas

### HU4 - Lista de Mediciones

- **URL:** `/measurements/`
- **Descripción:** Historial global de mediciones
- **Ordenamiento:** Por fecha descendente, últimas 50 registros

### HU5 - Resumen de Alertas

- **URL:** `/alerts/`
- **Descripción:** Alertas de la semana clasificadas por severidad
- **Categorías:** Grave, Alta, Media

### HU6-HU8 - Autenticación

- **Login:** `/login/` - Acceso directo sin validaciones
- **Registro:** `/register/` - Creación simplificada de cuentas
- **Recuperación:** `/password-reset/` - Vista demo sin funcionalidad

## Datos de Prueba

El sistema incluye datos de prueba precargados:

### Estadísticas

- **8 dispositivos** de diferentes categorías
- **680+ mediciones** de las últimas 2 semanas
- **6 alertas** de la semana actual
- **4 categorías:** Solar Panels, Wind Turbines, Battery Storage, Smart Meters
- **4 zonas:** Building A, Building B, Parking Lot, Roof Area

### Regenerar Datos (Opcional)

```bash
# Si necesitas recrear los datos de prueba
python manage.py seed_data
```

## Configuración para Desarrollo

### Variables de Entorno

```bash
# .env file
DEBUG=True
SECRET_KEY=tu-clave-secreta-aqui
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
```

### Comandos Útiles

```bash
# Crear nuevas migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser

# Acceder al admin
# URL: http://127.0.0.1:8000/admin/

# Shell de Django
python manage.py shell
```

## Flujo de Trabajo con Git

### Ramas Principales

- `main` - Código estable y funcional
- `feature/templates-autenticacion-matias` - Templates y frontend
- `feature/modelos-vistas-dispositivos-alma` - Backend y modelos

### Pull Requests

El proyecto incluye PRs que demuestran:

- Trabajo colaborativo entre desarrolladores
- Separación clara de responsabilidades
- Integración de funcionalidades complementarias

## Tecnologías Utilizadas

### Backend

- Django 5.2 (Framework web)
- SQLite (Base de datos)
- Python 3.11+ (Lenguaje principal)

### Frontend

- HTML5 (Estructura)
- CSS3 (Estilos y animaciones)
- JavaScript Vanilla (Interactividad)
- Diseño responsive sin frameworks externos

### Herramientas

- Git (Control de versiones)
- pip (Gestión de dependencias)
- Virtual environments (Aislamiento de dependencias)

## Notas para Evaluación

### Cumplimiento de Requisitos

- ✅ Modelos en inglés con campos obligatorios
- ✅ Relaciones correctas con Organization
- ✅ Todas las HU implementadas y funcionales
- ✅ Templates con Bootstrap básico
- ✅ Sistema de autenticación (simplificado)
- ✅ Repositorio Git con ramas y colaboración
- ✅ Estados vacíos manejados correctamente

### Consideraciones Especiales

- **Autenticación simplificada:** Para facilitar evaluación académica
- **Base de datos incluida:** Permite demo inmediata sin configuración
- **Datos realistas:** Generados para mostrar funcionalidades completas
- **Documentación completa:** README detallado y código comentado

### URLs Principales para Pruebas

```
http://127.0.0.1:8000/                    # Dashboard
http://127.0.0.1:8000/login/              # Login
http://127.0.0.1:8000/devices/            # Lista dispositivos
http://127.0.0.1:8000/devices/1/          # Detalle dispositivo
http://127.0.0.1:8000/measurements/       # Mediciones
http://127.0.0.1:8000/alerts/             # Alertas
http://127.0.0.1:8000/admin/              # Administración
```

## Solución de Problemas

### Error: No module named 'django'

```bash
# Activar entorno virtual
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### Error: No such table

```bash
# Aplicar migraciones
python manage.py migrate
```

### Error: Base de datos vacía

```bash
# Regenerar datos de prueba
python manage.py seed_data
```

## Contacto

- **Desarrolladores:** Matias y Alma
- **Repositorio:** [GitHub](https://github.com/mati-sly/ecoenergy-sistema-monitoreo-EVALUACION)
- **Institución:** Instituto Profesional AIEP - La Serena

---

## Licencia

Proyecto académico desarrollado para fines educativos.

**Desarrollado con 💚 para un futuro energético sostenible**
