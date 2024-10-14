# polizaInmueble.py

# PolizaInmueble

# Atributos de instancia:
# numero: entero
# incendio: real
# explosion: real
# robo: real

# Constructor:
# PolizaInmueble(numero: entero, incendio: real, explosion: real, robo: real)

# Comandos:
# No se especifican comandos en el diagrama

# Consultas:
# costoPoliza() -> real: Calcula el costo en caso de siniestro
# toString() -> string: Devuelve una representación en cadena de la póliza

# Métodos triviales:
# getNumero() -> entero: Devuelve el número de la póliza
# getIncendio() -> real: Devuelve el valor de cobertura por incendio
# getExplosion() -> real: Devuelve el valor de cobertura por explosión
# getRobo() -> real: Devuelve el valor de cobertura por robo

# polizaInmueble.py

class PolizaInmueble:
    def __init__(self, numero: int, incendio: float, explosion: float, robo: float):
        self.__numero = numero
        self.__incendio = incendio
        self.__explosion = explosion
        self.__robo = robo

    def getNumero(self) -> int:
        return self.__numero

    def setNumero(self, numero: int):
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("El número de póliza debe ser un entero positivo")
        self.__numero = numero

    def getIncendio(self) -> float:
        return self.__incendio

    def setIncendio(self, incendio: float):
        if incendio < 0:
            raise ValueError("El valor de cobertura por incendio debe ser no negativo")
        self.__incendio = incendio

    def getExplosion(self) -> float:
        return self.__explosion

    def setExplosion(self, explosion: float):
        if explosion < 0:
            raise ValueError("El valor de cobertura por explosión debe ser no negativo")
        self.__explosion = explosion

    def getRobo(self) -> float:
        return self.__robo

    def setRobo(self, robo: float):
        if robo < 0:
            raise ValueError("El valor de cobertura por robo debe ser no negativo")
        self.__robo = robo
    
    def costoPoliza(self) -> float:
        return self.__incendio + self.__explosion + self.__robo
    
    def __str__(self):
        return f"PolizaInmueble(numero={self.__numero}, incendio={self.__incendio}, explosion={self.__explosion}, robo={self.__robo})"
    
    
