# Guía de Aventura

#     Atributos:
#         nombre (String): Nombre del guía.
#         turno_trabajo (String): Turno de trabajo (mañana, tarde, noche).
        
#     Métodos:
#         autorizar_visitante(Visitante, Atracción): Método para autorizar a un visitante basado en su estatura y los requisitos de la atracción.

# Relaciones entre las clases:
#     La clase Visitante tiene una relación con Entrada ya que un visitante puede tener una o más entradas.
#     La clase Visitante también tiene una relación con Atracción, ya que se debe llevar un registro de las atracciones que el visitante ha disfrutado.

# guiaAventura.py

# Importa las clases Visitante y Atracción
from visitante import Visitante
from atraccion import Atraccion

class GuiaAventura:
    def __init__(self, nombre, turno_trabajo):
        # Validaciones:
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de caracteres")
        if not isinstance(turno_trabajo, str):
            raise ValueError("El turno de trabajo debe ser una cadena de caracteres")

        # Asignaciones:
        self.__nombre = nombre
        self.__turno_trabajo = turno_trabajo

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_turno_trabajo(self):
        return self.__turno_trabajo

    def set_turno_trabajo(self, turno_trabajo):
        self.__turno_trabajo = turno_trabajo
    
    def autorizar_visitante(self, visitante, atraccion):
        # Validaciones:
        if not isinstance(visitante, Visitante):
            raise ValueError("El visitante debe ser una instancia de la clase Visitante")
        if not isinstance(atraccion, Atraccion):
            raise ValueError("La atracción debe ser una instancia de la clase Atracción")

        # Asignaciones:
        if visitante.get_estatura() >= atraccion.get_estatura_minima():
            visitante.get_historial_atracciones().append(atraccion)
            print("El visitante ha sido autorizado")
            return True
        else:
            print("El visitante no cumple con los requisitos")
            return False
        
    def __str__(self):
        return f"Nombre: {self.__nombre}\nTurno de trabajo: {self.__turno_trabajo}"
