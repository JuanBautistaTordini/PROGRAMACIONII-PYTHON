# Visitante

#     Atributos:
#         nombre (String): Nombre del visitante.
#         edad (Int): Edad del visitante.
#         estatura (Double): Estatura del visitante.
#         correo_electronico (String): Dirección de correo electrónico.
#     Relaciones:
#         entradas (List<Entrada>): Lista de entradas compradas por el visitante.
#         historial_atracciones (List<Atracción>): Registro de atracciones que el visitante ha disfrutado.

# Relaciones entre las clases:
#     La clase Visitante tiene una relación con Entrada ya que un visitante puede tener una o más entradas.
#     La clase Visitante también tiene una relación con Atracción, ya que se debe llevar un registro de las atracciones que el visitante ha disfrutado.

class Visitante:
    def __init__(self, nombre: str, edad: int, estatura: float, correo_electronico: str):
        # Validaciones:
        if not isinstance(edad, int):
            raise ValueError("Edad debe ser un valor numérico")
        if not isinstance(estatura, float):
            raise ValueError("Estatura debe ser un valor numérico")
        if not isinstance(correo_electronico, str):  # Corrección realizada aquí
            raise ValueError("El correo electrónico debe ser una cadena de caracteres")
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de caracteres")

        # Asignaciones:
        self.__nombre = nombre
        self.__edad = edad
        self.__estatura = estatura
        self.__correo_electronico = correo_electronico  # Corrección realizada aquí
        # Entradas:
        self.__entradas = []
        # Atracciones:
        self.__historial_atracciones = []

    # Get y set
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_estatura(self):
        return self.__estatura

    def set_estatura(self, estatura):
        self.__estatura = estatura

    def get_correo_electronico(self):  # Corrección realizada aquí
        return self.__correo_electronico

    def set_correo_electronico(self, correo_electronico):  # Corrección realizada aquí
        self.__correo_electronico = correo_electronico

    def get_entradas(self):
        return self.__entradas

    def get_historial_atracciones(self):
        return self.__historial_atracciones

    def comprar_entrada(self, entrada):
        self.__entradas.append(entrada)

    def registrar_atracciones(self, atraccion):
        self.__historial_atracciones.append(atraccion)

    def __str__(self):
        return f"Nombre: {self.__nombre}\nEdad: {self.__edad}\nEstatura: {self.__estatura}\nCorreo Electrónico: {self.__correo_electronico}"

        