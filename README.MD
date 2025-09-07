# 🌱⚡ EcoEnergy - Sistema de Monitoreo (Versión Evaluación)

Sistema de monitoreo IoT simplificado para dispositivos de energía renovable desarrollado con Django.

## 📋 Descripción

Esta es una versión simplificada del sistema de monitoreo EcoEnergy, diseñada específicamente para demostración y evaluación académica. El sistema permite visualizar y gestionar dispositivos de monitoreo energético a través de una interfaz web intuitiva.

### ✨ Características Principales

- **Dashboard interactivo** con métricas de dispositivos
- **Gestión de dispositivos IoT** (CRUD completo)
- **Monitoreo de mediciones** en tiempo real
- **Sistema de alertas** básico
- **Autenticación simplificada** para demo
- **Interfaz responsive** compatible con móviles

## 🎯 Versión Demo

Esta versión está optimizada para evaluación y incluye:

- ✅ **Acceso directo sin credenciales** - Solo haz clic en "Iniciar Sesión"
- ✅ **Datos de ejemplo precargados** para demostración
- ✅ **Funcionalidades visuales completas** sin complejidad backend
- ✅ **Interfaz profesional** manteniendo el diseño original

## 🚀 Instalación Rápida

### Prerrequisitos

- Python 3.8+
- pip
- virtualenv (recomendado)

### Pasos de instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/mati-sly/ecoenergy-sistema-monitoreo-EVALUACION.git
cd ecoenergy-sistema-monitoreo-EVALUACION
```

2. **Crear entorno virtual**

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**

```bash
# Copia el template y ajusta si es necesario
cp .env.example .env
```

5. **Ejecutar migraciones**

```bash
cd monitoreo
python manage.py migrate
```

6. **Iniciar servidor**

```bash
python manage.py runserver
```

7. **Acceder al sistema**

- Abre tu navegador en `http://127.0.0.1:8000`
- Haz clic en "Iniciar Sesión" para acceso directo

## 📁 Estructura del Proyecto

```
ecoenergy-sistema-monitoreo-EVALUACION/
├── monitoreo/                 # Proyecto Django principal
│   ├── dispositivos/          # App principal de dispositivos
│   │   ├── models.py         # Modelos de datos
│   │   ├── views.py          # Lógica de vistas
│   │   └── templates/        # Templates HTML
│   ├── usuarios/             # App de autenticación
│   │   ├── views.py          # Login simplificado
│   │   └── templates/        # Templates de usuario
│   └── monitoreo/            # Configuración Django
├── requirements.txt          # Dependencias Python
├── .env.example             # Template de configuración
└── README.md               # Este archivo
```

## 🛠️ Tecnologías Utilizadas

- **Backend:** Django 5.2, Python 3.11
- **Base de datos:** SQLite (desarrollo)
- **Frontend:** HTML5, CSS3, JavaScript vanilla
- **Estilos:** CSS personalizado con gradientes y animaciones
- **Icons:** Emojis y símbolos Unicode

## 🎨 Características de la Interfaz

- **Diseño moderno** con gradientes ecológicos
- **Efectos glassmorphism** y transparencias
- **Animaciones suaves** en botones e interacciones
- **Paleta de colores** inspirada en energía limpia
- **Responsive design** para diferentes dispositivos

## 📊 Funcionalidades Demo

### Dashboard Principal

- Vista general de dispositivos activos
- Métricas básicas de monitoreo
- Gráficos de ejemplo

### Gestión de Dispositivos

- Lista de dispositivos con filtros
- Creación de nuevos dispositivos
- Edición y eliminación (simulada)

### Sistema de Monitoreo

- Visualización de mediciones
- Historial de datos
- Alertas básicas

## 🔧 Configuración de Desarrollo

Para desarrollo local, el sistema incluye:

- **Debug activado** por defecto
- **Base de datos SQLite** preconfigurada
- **Datos de ejemplo** para testing
- **Hot reload** para cambios en tiempo real

## 📝 Notas Importantes

- Esta es una **versión simplificada** para evaluación
- Las validaciones complejas están **deshabilitadas**
- Los datos son **simulados** para demostración
- No incluye funcionalidades de **producción real**

## 🔐 Autenticación Demo

El sistema incluye autenticación simplificada:

- **Login directo** sin credenciales
- **Usuario demo** creado automáticamente
- **Sesiones persistentes** durante la demostración

## 🎯 Casos de Uso Demostrados

1. **HU1:** Dashboard principal con métricas
2. **HU2:** Lista de dispositivos con filtros
3. **HU3:** Detalle individual de dispositivos
4. **HU4:** Gestión de mediciones
5. **HU5:** Sistema de alertas básico

## 📧 Contacto

Para consultas sobre este proyecto:

- **Desarrolladores:** Matias y Alma
- **Repositorio:** [GitHub](https://github.com/mati-sly/ecoenergy-sistema-monitoreo-EVALUACION)

---

## 📜 Licencia

Este proyecto es una demostración académica desarrollada para fines educativos.

---

_Desarrollado con 💚 para un futuro energético sostenible_
