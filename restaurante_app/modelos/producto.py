class Producto:
    """
    Clase que representa un producto del restaurante.
    Aplica el principio de Responsabilidad Única: esta clase solo se
    encarga de representar y validar los datos de un producto.
    """

    def __init__(
        self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0
    ) -> None:
        if not codigo:
            raise ValueError("El código del producto no puede estar vacío.")
        if not nombre:
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not categoria:
            raise ValueError("La categoría del producto no puede estar vacía.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio
        self.stock: int = stock

    def mostrar_informacion(self) -> str:
        """Devuelve la información del producto en formato texto."""
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )

    def a_diccionario(self) -> dict:
        """Convierte el producto en un diccionario compatible con JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
        }

    @staticmethod
    def desde_diccionario(datos: dict) -> "Producto":
        """Crea un objeto Producto a partir de un diccionario."""
        return Producto(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=datos["precio"],
            stock=datos.get("stock", 0),
        )