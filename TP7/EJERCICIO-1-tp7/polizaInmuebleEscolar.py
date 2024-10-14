# polizaInmuebleEscolar.py

# diagrama de clases:
# Diagrama de clases para PolizaInmuebleEscolar:

# PolizaInmuebleEscolar hereda de PolizaInmueble

# Atributos de instancia:
# - cantPersonas: entero
# - montoEquipamiento: real
# - montoMobiliario: real
# - montoPersona: real

# Constructor:
# No se especifica explícitamente en el diagrama

# Comandos:
# No se especifican comandos en el diagrama

# Consultas:
# - costoPoliza(): real
#   Calcula el costo en caso de siniestro
# - toString(): string
#   Devuelve una representación en cadena de la póliza

# Nota: La clase hereda los atributos y métodos de PolizaInmueble
# y agrega sus propios atributos específicos para inmuebles escolares.

from polizaInmueble import PolizaInmueble

class PolizaInmuebleEscolar(PolizaInmueble):
    def __init__(self, numero: int, incendio: float, explosion: float, robo: float, cantPersonas: int, montoEquipamiento: float, montoMobiliario: float, montoPersona: float):
        super().__init__(numero, incendio, explosion, robo)
        self.__cantPersonas = cantPersonas
        self.__montoEquipamiento = montoEquipamiento
        self.__montoMobiliario = montoMobiliario
        self.__montoPersona = montoPersona

    def getCantPersonas(self) -> int:
        return self.__cantPersonas

    def setCantPersonas(self, cantPersonas: int):
        if cantPersonas <= 0:
            raise ValueError("La cantidad de personas debe ser un entero positivo")
        self.__cantPersonas = cantPersonas

    def getMontoEquipamiento(self) -> float:
        return self.__montoEquipamiento

    def setMontoEquipamiento(self, montoEquipamiento: float):
        if montoEquipamiento < 0:
            raise ValueError("El monto de equipamiento debe ser no negativo")
        self.__montoEquipamiento = montoEquipamiento

    def getMontoMobiliario(self) -> float:
        return self.__montoMobiliario

    def setMontoMobiliario(self, montoMobiliario: float):
        if montoMobiliario < 0:
            raise ValueError("El monto de mobiliario debe ser no negativo")
        self.__montoMobiliario = montoMobiliario

    def getMontoPersona(self) -> float:
        return self.__montoPersona

    def setMontoPersona(self, montoPersona: float):
        if montoPersona < 0:
            raise ValueError("El monto por persona debe ser no negativo")
        self.__montoPersona = montoPersona

    def costoPoliza(self) -> float:
        return self.__montoEquipamiento + self.__montoMobiliario + (self.__cantPersonas * self.__montoPersona)
    
    def __str__(self) -> str:
        return (f"PolizaInmuebleEscolar(numero={self.getNumero()}, incendio={self.getIncendio()}, "
                f"explosion={self.getExplosion()}, robo={self.getRobo()}, cantPersonas={self.__cantPersonas}, "
                f"montoEquipamiento={self.__montoEquipamiento}, montoMobiliario={self.__montoMobiliario}, "
                f"montoPersona={self.__montoPersona})")


