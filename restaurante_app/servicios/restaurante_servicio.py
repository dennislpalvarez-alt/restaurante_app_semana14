from datetime import date
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class RestauranteServicio:
    """
    Convierte los datos cargados en objetos, valida el acceso y
    concentra las reglas de negocio y persistencia de productos y ventas.
    La interfaz nunca valida ni escribe JSON por su cuenta.
    """

    def __init__(self, archivo_servicio) -> None:
        self.archivo_servicio = archivo_servicio
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.ventas: list[Venta] = []  # Semana 15: lista de ventas en memoria
        self.cargar_datos()

    def cargar_datos(self) -> None:
        """Carga los datos persistidos y los convierte en objetos."""
        productos_json = self.archivo_servicio.leer_productos()
        usuarios_json = self.archivo_servicio.leer_usuarios()
        ventas_json = self.archivo_servicio.leer_ventas()  # Semana 15

        self.productos = [Producto.desde_diccionario(d) for d in productos_json]
        self.usuarios = [Usuario.desde_diccionario(d) for d in usuarios_json]

        # Semana 15: carga las ventas persistidas para mostrarlas en la interfaz
        self.ventas = [
            Venta(
                d.get("identificador", ""),
                d.get("usuario_id", ""),
                d.get("producto_codigo", ""),
                d.get("fecha", ""),
            )
            for d in ventas_json
        ]

    def validar_acceso(self, usuario: str, contrasena: str) -> Usuario | None:
        """Verifica si las credenciales coinciden con un usuario cargado."""
        for u in self.usuarios:
            if u.usuario == usuario and u.contrasena == contrasena:
                return u
        return None

    # ---------------- CONSULTAS GENERALES ----------------

    def listar_productos(self) -> list[Producto]:
        return self.productos

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios

    def listar_ventas(self) -> list[Venta]:  # Semana 15
        """Entrega las ventas cargadas para mostrarlas en la interfaz."""
        return self.ventas

    def cantidad_productos(self) -> int:
        return len(self.productos)

    def cantidad_usuarios(self) -> int:
        return len(self.usuarios)

    def cantidad_ventas(self) -> int:  # Semana 15
        return len(self.ventas)

    # ---------------- BÚSQUEDAS ----------------

    def buscar_producto(self, codigo: str) -> Producto | None:
        codigo = codigo.strip()
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        """Busca un usuario por su identificación (necesario para validar la venta)."""
        identificacion = identificacion.strip()
        for usuario in self.usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    # ---------------- CRUD DE PRODUCTOS (Semana 14) ----------------

    def registrar_producto(
        self, codigo: str, nombre: str, categoria: str, precio: str, stock: str
    ) -> Producto:
        if self.buscar_producto(codigo) is not None:
            raise ValueError("Ya existe un producto con ese codigo.")

        nuevo = Producto(
            codigo=codigo.strip(),
            nombre=nombre.strip(),
            categoria=categoria.strip(),
            precio=self._a_float(precio),
            stock=self._a_int(stock),
        )
        self.productos.append(nuevo)
        self.guardar_productos()
        return nuevo

    def actualizar_producto(
        self, codigo: str, nombre: str, categoria: str, precio: str, stock: str
    ) -> Producto:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError("No existe un producto con ese codigo.")

        datos_validados = Producto(
            codigo=codigo.strip(),
            nombre=nombre.strip(),
            categoria=categoria.strip(),
            precio=self._a_float(precio),
            stock=self._a_int(stock),
        )
        producto.nombre = datos_validados.nombre
        producto.categoria = datos_validados.categoria
        producto.precio = datos_validados.precio
        producto.stock = datos_validados.stock
        self.guardar_productos()
        return producto

    def eliminar_producto(self, codigo: str) -> Producto:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError("No existe un producto con ese codigo.")

        self.productos.remove(producto)
        self.guardar_productos()
        return producto

    def guardar_productos(self) -> None:
        self.archivo_servicio.guardar_productos(
            [producto.a_diccionario() for producto in self.productos]
        )

    # ---------------- VENTAS (Semana 15) ----------------

    def generar_identificador_venta(self) -> str:
        """Genera un identificador único para la venta (V001, V002...)."""
        siguiente = len(self.ventas) + 1
        return f"V{siguiente:03d}"

    def registrar_venta(self, usuario_id: str, producto_codigo: str) -> Venta:
        """
        Registra una venta. Valida que el usuario y el producto existan
        antes de crear el objeto Venta y persistirlo.
        """
        usuario_id = usuario_id.strip()
        producto_codigo = producto_codigo.strip()

        if not usuario_id:
            raise ValueError("Debe seleccionar un usuario.")
        if not producto_codigo:
            raise ValueError("Debe seleccionar un producto.")
        if self.buscar_usuario(usuario_id) is None:
            raise ValueError("El usuario seleccionado no existe.")
        if self.buscar_producto(producto_codigo) is None:
            raise ValueError("El producto seleccionado no existe.")

        nueva_venta = Venta(
            self.generar_identificador_venta(),
            usuario_id,
            producto_codigo,
            date.today().isoformat(),
        )
        self.ventas.append(nueva_venta)
        self.guardar_ventas()
        return nueva_venta

    def guardar_ventas(self) -> None:
        """Guarda la colección de ventas en el archivo JSON."""
        datos = [
            {
                "identificador": v.identificador,
                "usuario_id": v.usuario_id,
                "producto_codigo": v.producto_codigo,
                "fecha": v.fecha,
            }
            for v in self.ventas
        ]
        self.archivo_servicio.guardar_ventas(datos)

    # ---------------- AUXILIARES ----------------

    @staticmethod
    def _a_float(valor: str) -> float:
        try:
            return float(valor)
        except ValueError:
            raise ValueError("El precio debe ser un numero valido.")

    @staticmethod
    def _a_int(valor: str) -> int:
        try:
            return int(valor)
        except ValueError:
            raise ValueError("El stock debe ser un numero entero valido.")