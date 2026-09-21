class Usuario:
    """
    Clase que representa a una persona registrada en el sistema.
    Incluye credenciales de acceso (usuario/contraseña) para la
    simulación de inicio de sesión en la interfaz gráfica.
    Aplica Responsabilidad Única: solo representa los datos del usuario.
    """

    def __init__(
        self, identificacion: str, nombre: str, correo: str, usuario: str, contrasena: str
    ) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo
        self.usuario: str = usuario
        self.contrasena: str = contrasena

    def mostrar_informacion(self) -> str:
        """Devuelve la información del usuario en formato texto."""
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | Correo: {self.correo}"
        )

    @staticmethod
    def desde_diccionario(datos: dict) -> "Usuario":
        """Crea un objeto Usuario a partir de un diccionario."""
        return Usuario(
            identificacion=datos["identificacion"],
            nombre=datos["nombre"],
            correo=datos["correo"],
            usuario=datos["usuario"],
            contrasena=datos["contrasena"],
        )