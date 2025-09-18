# 🚀 Flask User Registration API

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/UI-Bootstrap-7952B3?logo=bootstrap&logoColor=white)
![MySQL](https://img.shields.io/badge/Database-MySQL-4479A1?logo=mysql&logoColor=white)
![DAO](https://img.shields.io/badge/Pattern-DAO-FF6B6B)

> *"Sistema de registro de usuarios con arquitectura escalable, MySQL y interfaz moderna"*

## 🌟 Características Principales

### 🎯 Funcionalidades CRUD
- ✅ **Crear usuarios** con validación de formularios
- 📋 **Listar usuarios** en tabla responsive
- ✏️ **Editar registros** de los usuarios por ID
- 🗑️ **Eliminar usuarios** para su gestion de registros

## 🧑‍💻 Clonacion del Proyecto
```bash
# Clonar repositorio
git clone https://github.com/Astharmin/Login_UserApp.git

# Configurar conexión MySQL en Cliente_DAO.py
# Ejecutar aplicación
python app.py
```

## 🏗️ Arquitectura Profesional
```mermaid
graph TB
    A[Frontend Bootstrap] --> B[Flask App]
    B --> C[WTForms Validation]
    B --> D[DAO Pattern]
    D --> E[MySQL Connector]
    E --> F[MySQL Database]
```
