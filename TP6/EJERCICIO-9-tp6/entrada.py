# Entrada

#     Atributos:
#         numero_entrada (Int): Número de la entrada.
#         fecha (Date): Fecha de compra o validez.
#         tipo (String): Tipo de entrada (e.g., general, VIP).
#     Relaciones:
#         visitante (Visitante): Asociada a un visitante específico.

# Relaciones entre las clases:
#     La clase Visitante tiene una relación con Entrada ya que un visitante puede tener una o más entradas.
#     La clase Visitante también tiene una relación con Atracción, ya que se debe llevar un registro de las atracciones que el visitante ha disfrutado.

from visitante import Visitante

# entrada.py

# Importa la clase Visitante
from visitante import Visitante

class Entrada:
    def __init__(self, numero_entrada: int, fecha: str, tipo: str, visitante):
        # Validaciones:
        if not isinstance(numero_entrada, int):
            raise ValueError("El número de entrada debe ser un valor numérico")
        if not isinstance(fecha, str):
            raise ValueError("La fecha debe ser una cadena de caracteres")
        if not isinstance(tipo, str):
            raise ValueError("El tipo de entrada debe ser una cadena de caracteres")
        if not isinstance(visitante, Visitante):
            raise ValueError("El visitante debe ser una instancia de la clase Visitante")

        # Asignaciones:
        self.__numero_entrada = numero_entrada
        self.__fecha = fecha
        self.__tipo = tipo
        self.__visitante = visitante

    def get_numero_entrada(self):
        return self.__numero_entrada

    def set_numero_entrada(self, numero_entrada):
        self.__numero_entrada = numero_entrada

    def get_fecha(self):
        return self.__fecha

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_visitante(self):
        return self.__visitante

    def set_visitante(self, visitante):
        self.__visitante = visitante
    
    def __str__(self):
        return f"Numero de entrada: {self.__numero_entrada}\nFecha: {self.__fecha}\nTipo: {self.__tipo}\nVisitante: {self.__visitante}"
