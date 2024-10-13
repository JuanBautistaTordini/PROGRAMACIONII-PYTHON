# Atracción

#     Atributos:
#     nombre (String): Nombre de la atracción.
#     tipo (String): Tipo de atracción (e.g., montaña rusa, casa embrujada).
#     nivel_de_emocion (String): Nivel de emoción (bajo, medio, alto).
#     estatura_minima (Double): Estatura mínima requerida para acceder.
#     turnos_funcionamiento (List<String>): Lista de turnos en los que funciona (e.g., mañana, tarde, noche).
    
# Visitante

#     Atributos:
#         nombre (String): Nombre del visitante.
#         edad (Int): Edad del visitante.
#         estatura (Double): Estatura del visitante.
#         correo_electronico (String): Dirección de correo electrónico.
#     Relaciones:
#         entradas (List<Entrada>): Lista de entradas compradas por el visitante.
#         historial_atracciones (List<Atracción>): Registro de atracciones que el visitante ha disfrutado.
        
# Entrada

#     Atributos:
#         numero_entrada (Int): Número de la entrada.
#         fecha (Date): Fecha de compra o validez.
#         tipo (String): Tipo de entrada (e.g., general, VIP).
#     Relaciones:
#         visitante (Visitante): Asociada a un visitante específico.
        
# Guía de Aventura

#     Atributos:
#         nombre (String): Nombre del guía.
#         turno_trabajo (String): Turno de trabajo (mañana, tarde, noche).
        
#     Métodos:
#         autorizar_visitante(Visitante, Atracción): Método para autorizar a un visitante basado en su estatura y los requisitos de la atracción.

# Relaciones entre las clases:
#     La clase Visitante tiene una relación con Entrada ya que un visitante puede tener una o más entradas.
#     La clase Visitante también tiene una relación con Atracción, ya que se debe llevar un registro de las atracciones que el visitante ha disfrutado.
#     La clase Guía de Aventura tiene una relación con Atracción para autorizar el acceso de visitantes a las atracciones.

#Clase Atracción:

class Atraccion:
    def __init__(self, nombre, tipo, nivel_de_emocion, estatura_minima, turnos_funcionamiento):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__nivel_de_emocion = nivel_de_emocion
        self.__estatura_minima = estatura_minima
        self.__turnos_funcionamiento = turnos_funcionamiento

    # getters y setters:
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_nivel_de_emocion(self):
        return self.__nivel_de_emocion

    def set_nivel_de_emocion(self, nivel_de_emocion):
        self.__nivel_de_emocion = nivel_de_emocion

    def get_estatura_minima(self):
        return self.__estatura_minima

    def set_estatura_minima(self, estatura_minima):
        self.__estatura_minima = estatura_minima

    def get_turnos_funcionamiento(self):
        return self.__turnos_funcionamiento

    def set_turnos_funcionamiento(self, turnos_funcionamiento):
        self.__turnos_funcionamiento = turnos_funcionamiento
    
    def __str__(self):
        return f"Atracción: {self.__nombre}\nTipo: {self.__tipo}\nNivel de Emoción: {self.__nivel_de_emocion}\nEstatura Minima: {self.__estatura_minima}\nTurnos de Funcionamiento: {self.__turnos_funcionamiento}"
    


    