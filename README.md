# 🍽️ Restaurante App — Semana 14

## Propósito
Segunda iteración del proyecto **restaurante_app** con una **interfaz gráfica mejorada** construida con **Tkinter**. 
Esta semana se implementa un **menú lateral de navegación**, se optimiza el **layout con contenedores** y se completa 
el **CRUD de Productos** directamente desde la interfaz gráfica.

##  Novedades - Semana 14

### ✅ Menú Lateral (Sidebar)
- Navegación intuitiva entre las diferentes secciones de la aplicación
- Diseño colapsable y responsivo
- Acceso rápido a: Productos, Usuarios y Ventas

### ✅ Layout con Contenedores
- Organización visual mejorada usando frames y contenedores
- Separación clara entre áreas de navegación y contenido
- Mejor experiencia de usuario (UX)

### ✅ CRUD de Productos Completo vía UI
- **Crear**: Registrar nuevos productos con validación de campos
- **Leer**: Visualizar lista completa de productos registrados
- **Actualizar**: Modificar información de productos existentes
- **Eliminar**: Eliminar productos con confirmación
- Feedback visual en cada operación

## Estructura del Proyecto

restaurante_app_semana14/
└── restaurante_app/
├── datos/
│ ├── productos.json # Base de datos de productos
│ └── usuarios.json # Usuarios y credenciales
├── modelos/
│ ├── producto.py # Entidad Producto
│ └── usuario.py # Entidad Usuario
├── servicios/
│ ├── archivo_servicio.py # Lectura/escritura de JSON
│ └── restaurante_servicio.py # Lógica de negocio
├── ui/
│ ├── login_view.py # Vista de inicio de sesión
│ └── main_view.py # Vista principal con menú lateral
└── main.py # Punto de entrada


## Responsabilidades

- **modelos/**: Representan las entidades del dominio (Producto, Usuario) con sus atributos y métodos.
- **servicios/archivo_servicio.py**: Lectura y escritura de archivos JSON sin lógica de negocio.
- **servicios/restaurante_servicio.py**: 
  - Convierte datos JSON en objetos del dominio
  - Valida credenciales de usuario
  - Gestiona operaciones CRUD de productos
  - Expone métodos que la UI consume
- **ui/**: 
  - Construye vistas con Tkinter
  - Implementa menú lateral de navegación
  - Utiliza contenedores (Frames) para organizar el layout
  - Solicita datos al servicio, nunca accede directamente a JSON
- **main.py**: Crea la ventana principal y controla el flujo entre LoginView y MainView.

## Flujo de la Aplicación

Inicio
│
├──> main.py inicializa Tkinter y servicios
│
├──> LoginView
│ ├── Usuario ingresa credenciales
│ └── RestauranteServicio valida acceso
│
├──> MainView (con menú lateral)
│ ├── Sección Productos
│ │ ├── Listar productos
│ │ ├── Crear producto
│ │ ├── Editar producto
│ │ └── Eliminar producto
│ │
│ ├── Sección Usuarios (visualización)
│ │
│ └── Sección Ventas (pendiente)
│
└──> Cerrar sesión → LoginView


## Características Técnicas

### Menú Lateral
- Implementado con `tkinter.Frame`
- Botones de navegación con estilos consistentes
- Highlight de sección activa

### Contenedores y Layout
- Uso de `pack()` y `grid()` para organización
- Frames anidados para separar áreas funcionales
- Espaciado y padding optimizados

### CRUD de Productos
- Formularios con validación de campos obligatorios
- Tabla/listado de productos con scroll
- Mensajes de confirmación y errores
- Actualización en tiempo real del archivo JSON

## Cómo Ejecutar

1. **Ubicarse en la carpeta del proyecto**:
   ```bash
   cd restaurante_app_semana14/restaurante_app
   
Ejecutar el punto de entrada:
   python main.py

Iniciar sesión con las credenciales de prueba:
Usuario: jperez
Contraseña: 1234
Navegar por el menú lateral y probar el CRUD de productos

Datos de Prueba
Usuario de Prueba
Registrado en datos/usuarios.json:

{
  "usuario": "jperez",
  "contrasena": "1234",
  "nombre": "Juan Pérez",
  "rol": "administrador"
}

Productos de Ejemplo
Puedes agregar productos iniciales en datos/productos.json o crearlos desde la UI.
Requisitos Técnicos
Python 3.8 o superior
Tkinter (viene incluido con Python)
Sistema operativo: Windows/macOS/Linux
Próximas Funcionalidades (Semanas Futuras)
CRUD completo de Usuarios
Módulo de Ventas funcional
Reportes y estadísticas
Búsqueda y filtrado de productos
Mejoras en la interfaz (imágenes, iconos)
Referencias
Estructura adaptada del proyecto docente Biblioteca App (Semana 13)

Autor
Dennis Pacheco - Proyecto académico de Programación Orientada a Objetos 