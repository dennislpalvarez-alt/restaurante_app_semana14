from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:
    """
    Convierte los datos cargados en objetos, valida el acceso y
    concentra las reglas de negocio y persistencia de productos.
    La interfaz nunca valida ni escribe JSON por su cuenta.
    """

    def __init__(self, archivo_servicio) -> None:
        self.archivo_servicio = archivo_servicio
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.cargar_datos()

    def cargar_datos(self) -> None:
        productos_json = self.archivo_servicio.leer_productos()
        usuarios_json = self.archivo_servicio.leer_usuarios()
        self.productos = [Producto.desde_diccionario(d) for d in productos_json]
        self.usuarios = [Usuario.desde_diccionario(d) for d in usuarios_json]

    def validar_acceso(self, usuario: str, contrasena: str) -> Usuario | None:
        for u in self.usuarios:
            if u.usuario == usuario and u.contrasena == contrasena:
                return u
        return None

    def listar_productos(self) -> list[Producto]:
        return self.productos

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios

    def cantidad_productos(self) -> int:
        return len(self.productos)

    def cantidad_usuarios(self) -> int:
        return len(self.usuarios)

    # ---------------- CRUD DE PRODUCTOS ----------------

    def buscar_producto(self, codigo: str) -> Producto | None:
        codigo = codigo.strip()
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

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