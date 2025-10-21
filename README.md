# 🦙 Fauna de Chile - Proyecto Django

Aplicación web desarrollada con Django para catalogar y administrar información sobre la fauna nativa de Chile.

## 📋 Descripción

Este proyecto es una aplicación web educativa que permite visualizar, agregar y gestionar información sobre los animales nativos de Chile. Incluye un sistema de autenticación y un panel de administración para controlar el contenido.

## ✨ Características

- 📱 Interfaz web responsive y amigable
- 🔐 Sistema de autenticación de usuarios
- ➕ Formulario para agregar nuevos animales (solo usuarios autenticados)
- 🗂️ Panel de administración completo
- 📊 Visualización dinámica de información
- 🔍 Búsqueda y filtrado de animales en el panel admin

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Django 4.x**
- **SQLite** (Base de datos)
- **HTML/CSS** (Frontend)

## 📦 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/moisesdatasci/fauna-chile.git
cd fauna-chile
```

2. **Crear entorno virtual** (recomendado)
```bash
python -m venv venv

# En Windows
venv\Scripts\activate

# En Mac/Linux
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install django
```

4. **Realizar migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario**
```bash
python manage.py createsuperuser
```

6. **Iniciar servidor**
```bash
python manage.py runserver
```

7. **Acceder a la aplicación**
- Página principal: http://127.0.0.1:8000/
- Panel admin: http://127.0.0.1:8000/admin/

## 📂 Estructura del Proyecto

```
fauna_chile/
│
├── fauna_chile/              # Configuración principal del proyecto
│   ├── settings.py          # Configuraciones
│   ├── urls.py              # URLs principales
│   └── wsgi.py
│
├── animales/                # Aplicación principal
│   ├── migrations/          # Migraciones de base de datos
│   ├── templates/           # Plantillas HTML
│   │   ├── animales/
│   │   │   ├── lista_animales.html
│   │   │   └── agregar_animal.html
│   │   └── registration/
│   │       └── login.html
│   ├── admin.py            # Configuración del panel admin
│   ├── models.py           # Modelos de datos
│   ├── views.py            # Vistas y lógica
│   ├── forms.py            # Formularios
│   └── urls.py             # URLs de la app
│
├── db.sqlite3              # Base de datos
└── manage.py               # Script de gestión Django
```

## 🗄️ Modelo de Datos

### Animal
- `nombre`: Nombre común del animal
- `nombre_cientifico`: Nombre científico (taxonomía)
- `habitat`: Descripción del hábitat natural
- `estado_conservacion`: Estado actual de conservación
- `descripcion`: Descripción detallada del animal
- `imagen_url`: URL de imagen (opcional)

## 🔑 Funcionalidades por Rol

### Usuario No Autenticado
- ✅ Ver lista de animales
- ✅ Ver detalles de cada animal

### Usuario Autenticado
- ✅ Todo lo anterior
- ✅ Agregar nuevos animales mediante formulario
- ✅ Cerrar sesión

### Administrador
- ✅ Todo lo anterior
- ✅ Acceso al panel de administración completo
- ✅ Editar y eliminar animales
- ✅ Gestionar usuarios y permisos
- ✅ Búsqueda y filtrado avanzado

## 🚀 Uso

### Agregar Animales

**Opción 1: Panel de Administración**
1. Accede a http://127.0.0.1:8000/admin/
2. Inicia sesión con tu superusuario
3. Click en "Animales" → "+ Agregar"
4. Completa el formulario y guarda

**Opción 2: Formulario Web**
1. Inicia sesión en la página principal
2. Click en "Agregar Animal"
3. Completa el formulario y guarda

**Opción 3: Django Shell**
```bash
python manage.py shell
```
```python
from animales.models import Animal

Animal.objects.create(
    nombre="Pudú",
    nombre_cientifico="Pudu puda",
    habitat="Bosques templados del sur de Chile",
    estado_conservacion="Vulnerable",
    descripcion="El pudú es el ciervo más pequeño del mundo."
)
```

## 🐾 Animales de Ejemplo

Algunos animales nativos de Chile que puedes agregar:

- **Pudú** - *Pudu puda* (Vulnerable)
- **Cóndor Andino** - *Vultur gryphus* (Casi amenazado)
- **Huemul** - *Hippocamelus bisulcus* (En peligro)
- **Pingüino de Humboldt** - *Spheniscus humboldti* (Vulnerable)
- **Zorro Culpeo** - *Lycalopex culpaeus* (Preocupación menor)
- **Puma** - *Puma concolor* (Preocupación menor)
- **Vicuña** - *Vicugna vicugna* (Preocupación menor)
- **Flamenco Chileno** - *Phoenicopterus chilensis* (Casi amenazado)

## 🔒 Seguridad

- ✅ Protección CSRF en formularios
- ✅ Autenticación requerida para agregar contenido
- ✅ Sistema de permisos integrado de Django
- ✅ Contraseñas hasheadas automáticamente

## 📝 Requerimientos Funcionales Cumplidos

- [x] Investigación sobre características de Django
- [x] Configuración de proyecto web Django
- [x] Implementación de templates con contenido dinámico
- [x] Formularios para captura y procesamiento de datos
- [x] Sistema de autenticación y autorización
- [x] Módulo de administración personalizado

## 🤝 Contribuir

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 👨‍💻 Autor

**Moisés Ortega**
- GitHub: [@tu-usuario](https://github.com/tu-usuario)

---

🦙 Hecho con ❤️ para la conservación de la fauna chilena
