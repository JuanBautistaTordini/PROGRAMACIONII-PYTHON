# main.py

from guiaAventura import GuiaAventura
from atraccion import Atraccion
from visitante import Visitante
from entrada import Entrada


# Crear algunas atracciones

#nombre, tipo, nivel_de_emocion, estatura_minima, turnos_funcionamiento (Lista de turnos (e.g., ["mañana", "tarde"]))

atraccion1 = Atraccion("Casa embrujada", "casa embrujada", "bajo", 1.70, ["mañana", "tarde"])
atraccion2 = Atraccion("Montaña rusa", "montaña rusa", "bajo", 1.70, ["mañana", "tarde"])

# Crear un visitante:

# nombre: str, edad: int, estatura: float, correo_electronico: str)

visitante1 = Visitante("Pepe", 20, 1.70, "pepe@pe.pe")

# crear entrada de visitante (self.__entradas = [])

entrada1 = Entrada(1, "2022-01-01", "general", visitante1)

# crear una guia de aventura:

#(self, nombre, turno_trabajo):

guia1 = GuiaAventura("Juan", "mañana")

#Autorizar visitante para montaña rusa:

guia1.autorizar_visitante(visitante1, atraccion2)

# autorizar visitante para casa embrujada:

guia1.autorizar_visitante(visitante1, atraccion1)