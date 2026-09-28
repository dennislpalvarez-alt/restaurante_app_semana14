# Restaurante App — Semana 14

## Propósito
Segunda iteración del proyecto **restaurante_app** con una **interfaz gráfica mejorada** construida con **Tkinter**.
Esta semana se implementa un **menú lateral de navegación**, se organiza el **layout con contenedores** y se completa
el **CRUD de Productos** directamente desde la interfaz gráfica.

## Novedades — Semana 14

### Menú lateral (sidebar)
- Navegación entre secciones: Inicio, Usuarios, Productos y Cerrar sesión.
- Resalta visualmente la sección activa.

### Layout con contenedores
- Organización visual mediante `Frame` y `LabelFrame`.
- Separación clara entre menú de navegación, formulario y área de contenido.

### CRUD de productos completo vía UI
- **Crear**: registrar nuevos productos con validación de campos.
- **Leer**: visualizar la lista completa de productos registrados y cargar uno por código.
- **Actualizar**: modificar los datos de un producto existente.
- **Eliminar**: eliminar un producto por código.
- Mensajes de confirmación y de error en cada operación.

## Estructura del proyecto

```
restaurante_app_semana14/
├── restaurante_app/
│   ├── datos/
│   │   ├── productos.json
│   │   └── usuarios.json
│   ├── modelos/
│   │   ├── producto.py
│   │   └── usuario.py
│   ├── servicios/
│   │   ├── archivo_servicio.py
│   │   └── restaurante_servicio.py
│   ├── ui/
│   │   ├── login_view.py
│   │   └── main_view.py
│   └── main.py
└── README.md
```

## Responsabilidades
- **modelos/**: representan las entidades del dominio (Producto, Usuario).
- **servicios/archivo_servicio.py**: lee y escribe los archivos JSON, sin lógica de negocio.
- **servicios/restaurante_servicio.py**: convierte los datos en objetos, valida el acceso, y concentra las reglas y la persistencia del CRUD de productos.
- **ui/**: construye las vistas con Tkinter (menú lateral, formularios, tablas) y solicita todo al servicio; nunca lee ni escribe JSON directamente.
- **main.py**: crea la única ventana `Tk()` y controla el cambio entre `LoginView` y `MainView`.

## Flujo de la aplicación

```
Inicio de la aplicacion
        |
main.py prepara Tkinter y los servicios
        |
   LoginView
        |
RestauranteServicio valida el acceso
        |
    MainView (menu lateral)
        |
Inicio | Usuarios (consulta) | Productos (CRUD)
        |
Registrar / Cargar / Actualizar / Eliminar producto
        |
RestauranteServicio procesa y guarda en productos.json
        |
   Cerrar sesion
        |
   LoginView
```

## Cómo ejecutar

1. Ubicarse dentro de la carpeta `restaurante_app`:
   ```
   cd restaurante_app
   ```
2. Ejecutar el punto de entrada:
   ```
   python main.py
   ```
3. Iniciar sesión con el usuario de prueba cargado en `datos/usuarios.json`:
   - Usuario: `jperez`
   - Contraseña: `1234`
4. Navegar por el menú lateral y probar el CRUD de productos.

## Requisitos técnicos
- Python 3.8 o superior
- Tkinter (incluido con Python)

## Referencias
Estructura y flujo adaptados de los proyectos docentes *Biblioteca App* (Semana 13 y Semana 14):
- https://github.com/kevin10lascano-sketch/Clase-Semana-13-POO.git
- https://github.com/kevin10lascano-sketch/Clase-Semana-14-POO.git

## Autor
Dennis Leonardo Pacheco Álvarez — Proyecto académico de Programación Orientada a Objetos.