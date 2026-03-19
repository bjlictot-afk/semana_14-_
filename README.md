# semana_14-_
# 📋 Sistema de Registro de Visitantes

Aplicación de escritorio desarrollada en **Python** utilizando **Tkinter**, que permite gestionar el registro de visitantes en una oficina mediante operaciones CRUD (Crear, Leer, Eliminar).

Este proyecto implementa una **arquitectura modular por capas**, separando claramente la lógica de negocio, los datos y la interfaz gráfica.

---

## 🎯 Objetivo

Desarrollar una aplicación que permita:

* Registrar nuevos visitantes
* Visualizar los registros en una tabla
* Eliminar visitantes seleccionados
* Limpiar los campos del formulario

---

## 🧱 Arquitectura del Proyecto

El sistema está organizado en las siguientes capas:

```
visitas_app/
│
├── main.py
├── modelos/
│   └── visitante.py
├── servicios/
│   └── visita_servicio.py
└── ui/
    └── app_tkinter.py
```

### 🔹 Descripción de capas

* **Modelos:** Define la estructura de los datos (Visitante).
* **Servicios:** Contiene la lógica del sistema (CRUD).
* **UI:** Interfaz gráfica con Tkinter.
* **Main:** Punto de entrada de la aplicación.

---

## ⚙️ Tecnologías utilizadas

* Python 3
* Tkinter (interfaz gráfica)
* ttk (componentes avanzados como tablas)

---

## 🧩 Funcionalidades

✔ Registro de visitantes
✔ Validación de campos obligatorios
✔ Prevención de cédulas duplicadas
✔ Visualización en tabla dinámica (Treeview)
✔ Eliminación de registros
✔ Limpieza automática de campos

---

## ▶️ Cómo ejecutar el programa

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/tarea_poo_visitas.git
```

2. Ingresar al proyecto:

```bash
cd tarea_poo_visitas
```

3. Ejecutar la aplicación:

```bash
python main.py
```

---

## 🧪 Requisitos

* Tener instalado Python 3.x
* No se requieren librerías externas

---

## 🧑‍💻 Autor

* Nombre: (Tu nombre aquí)
* Curso: Programación Orientada a Objetos

---

## 📌 Notas

Este proyecto fue desarrollado con fines académicos para demostrar:

* Uso de Programación Orientada a Objetos (POO)
* Separación de responsabilidades (arquitectura por capas)
* Implementación de interfaces gráficas en Python

---
