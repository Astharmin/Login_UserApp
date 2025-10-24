# 🚀 **Sistema de Gestión de Clientes - Flask Web App**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql&logoColor=white)
![DAO Pattern](https://img.shields.io/badge/Pattern-DAO-FF6B6B)
![Security](https://img.shields.io/badge/Security-Env%20Vars-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

> *"Aplicación web segura para gestión de clientes con configuración cifrada, pool de conexiones y arquitectura empresarial"*

---

## 🌟 **Características Principales**

### 🎨 **Interfaz de Usuario Moderna**
- ✅ **Diseño responsive** con Bootstrap 5.3
- 🎯 **Tema oscuro** integrado
- 📱 **Interfaz intuitiva** y fácil de usar
- ⚡ **Navegación fluida** sin recargas

### 🔧 **Funcionalidades CRUD Completas**
- 👥 **Agregar nuevos clientes** con formularios validados
- 📋 **Listar todos los clientes** en tabla interactiva
- ✏️ **Editar información** con pre-carga de datos
- 🗑️ **Eliminar clientes** con confirmación visual
- 🧹 **Limpiar formularios** rápidamente

### 🔒 **Seguridad Avanzada**
- 🛡️ **Configuración cifrada** con variables de entorno
- 🔐 **Pool de conexiones** seguro y eficiente
- 📝 **Credenciales protegidas** en archivo .env
- 💾 **Persistencia robusta** con MySQL

---

## 🏗️ **Arquitectura del Sistema**

```mermaid
graph TB
    A[Templates Bootstrap] --> B[Flask App]
    B --> C[ClienteDAO]
    C --> D[Pool Conexiones]
    D --> E[MySQL Database]
    
    F[WTForms] --> B
    G[.env Config] --> D
    H[Modelo Cliente] --> C
```

---

## 📁 **Estructura del Proyecto**

```
sistema-clientes-web/
├── app.py                 # 🚀 Aplicación Flask principal
├── Cliente.py            # 📊 Modelo de datos Cliente
├── ClienteDAO.py         # 🏗️ Data Access Object
├── Conexion.py           # 🔌 Pool de conexiones seguro
├── cliente_form.py       # 📝 Formularios WTForms
├── requirements.txt      # 📦 Dependencias
├── templates/           # 🎨 Frontend
│   └── index.html      # 🏠 Página principal
└── README.md           # 📚 Documentación
```

---

## 🛠️ **Tecnologías Utilizadas**

### 🔧 Backend & Seguridad
- **Python 3.8+** - Lenguaje principal
- **Flask** - Microframework web
- **WTForms** - Validación de formularios
- **python-dotenv** - Gestión de variables entorno
- **mysql-connector-pool** - Pool de conexiones

### 🎨 Frontend
- **Bootstrap 5.3** - Framework CSS
- **Bootstrap Icons** - Iconografía moderna
- **HTML5** - Estructura semántica
- **Jinja2** - Motor de templates

### 🗄️ Base de Datos
- **MySQL 8.0+** - Base de datos relacional
- **Connection Pooling** - Gestión eficiente
- **Patrón DAO** - Acceso abstracto a datos

---

## 🚀 **Instalación y Configuración**

### Prerrequisitos
```bash
# Python 3.8 o superior
python --version

# MySQL 8.0+
mysql --version
```

### ⚡ **Configuración Segura**
```bash
# 1. Clonar repositorio
git clone https://github.com/Astharmin/login-userapp.git
cd login-userapp

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales seguras

# 5. Ejecutar aplicación
python app.py
```

---

## 💾 **Esquema de Base de Datos**

```sql
CREATE TABLE cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    mail VARCHAR(255) UNIQUE NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🎯 **Ventajas de la Arquitectura Segura**

### 🔐 **Seguridad Empresarial**
- **Credenciales nunca en código** - Variables de entorno
- **Pool de conexiones** - Prevención de ataques DDoS
- **Validación de datos** - Prevención de inyecciones SQL
- **CSRF Protection** - Protección contra ataques cross-site

### ⚡ **Performance Optimizado**
- **Connection Pooling** - Reutilización de conexiones
- **Conexiones pre-establecidas** - Reducción de latencia
- **Gestión automática** de recursos

### 🔧 **Configuración para Producción**
```python
# Configuración lista para deployment
load_dotenv()  # Carga automática según entorno

class Conexion:
    DATABASE = os.getenv('DB_NAME', 'fallback_db')
    USERNAME = os.getenv('DB_USER', 'fallback_user')
    # ... resto de configuración segura
```

---

## 🎨 **Características de la Interfaz**

### ✨ **Diseño Moderno**
- **Tema oscuro** por defecto
- **Grid responsive** de 2 columnas
- **Tablas con hover effects**
- **Iconos Bootstrap** integrados

### 🔄 **Interacción Intuitiva**
```html
<!-- Formulario con validación -->
<div class="form-floating py-2">
    {{forma.nombre(class="form-control", placeholder="Nombre")}}
    {{forma.nombre.label}}
</div>

<!-- Tabla interactiva -->
<table class="table table-striped table-hover">
    <thead class="table-info">
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Mail</th>
            <th>Acciones</th>
        </tr>
    </thead>
</table>
```

---

## 🔧 **Endpoints de la Aplicación**

| Ruta | Método | Descripción | Seguridad |
|------|--------|-------------|-----------|
| `/` | GET | Página principal | Pública |
| `/guardar` | POST | Guardar/Actualizar cliente | CSRF Token |
| `/editar/<id>` | GET | Cargar datos cliente | Validación ID |
| `/eliminar/<id>` | GET | Eliminar cliente | Validación ID |
| `/limpiar` | GET | Limpiar formulario | Pública |

---

## 🚀 **Deployment Preparado**

### ☁️ **Listo para Producción**
- **Variables de entorno** para diferentes ambientes
- **Pool de conexiones** configurable
- **Error handling** robusto
- **Logging** para monitorización

### 🔄 **Escalabilidad**
```python
# Pool size configurable por entorno
POOL_SIZE = int(os.getenv('POOL_SIZE', 5))  # Desarrollo: 5, Producción: 20
```

---

## 🤝 **Contribución**

¿Te gustaría mejorar esta aplicación?

1. **Fork** el repositorio
2. Configura tu **.env** local
3. Crea una **rama feature** (`git checkout -b feature/NuevaCaracteristica`)
4. **Commit** tus cambios (`git commit -m 'Agregar NuevaCaracteristica'`)
5. **Push** a la rama (`git push origin feature/NuevaCaracteristica`)
6. Abre un **Pull Request**

**⚠️ Importante:** Nunca commits archivos .env con credenciales reales.

---

## 📄 **Licencia**

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

<div align="center">

### ⭐ ¿Te gustó este proyecto? ¡Déjame una estrella en GitHub!

**Desarrollado con ❤️ por [Astharmin](https://github.com/Astharmin)**

```mermaid
graph LR
    A[Flask App] --> B[Pool Seguro]
    B --> C[MySQL DB]
    C --> D[.env Config]
    D --> E[🚀 Producción]
```

*"Seguridad desde el diseño, performance desde la arquitectura"*

</div>
