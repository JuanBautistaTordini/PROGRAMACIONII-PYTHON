# Aseguradora.py

# Atributos de Instancia:
    # seguros: PolizaInmueble[]
# Constructor:
    # Aseguradora()

# Comandos:
    #Insertar(poliza: PolizaInmueble)
    #Eliminar(poliza: PolizaInmueble)
# Consultas:
    #existePoliza(poliza: PolizaInmueble) -> bool
    #hayPolizas() -> bool
    #costoTotal() -> float
    #esIgual(aseguradora: Aseguradora)
    
# Comandos:
    # insertar(poliza: PolizaInmueble) agrega una poliza a la lista, y mantiene ordenada la lista de pólizas por el número de póliza
    # eliminar(poliza: PolizaInmueble) elimina la póliza de la lista sólo si existe una póliza con la misma identidad que la recibida por parámetro
    
# Consultas:
    # esIgual(aseguradora: Aseguradora) retorna true si las dos colecciones mantienen referencias a los mismos objetos


from polizaInmueble import PolizaInmueble

class Aseguradora:
    def __init__(self):
        self.__seguros = []  # Atributo Privado

    def insertar(self, poliza: PolizaInmueble):
        '''Agrega una póliza a la lista, manteniendo ordenada la lista por el número de póliza'''
        if not isinstance(poliza, PolizaInmueble):
            raise ValueError("La póliza debe ser una instancia de PolizaInmueble")
        self.__seguros.append(poliza)
        self.__seguros.sort(key=lambda p: p.getNumero())  # Ordenar por número de póliza

    def eliminar(self, poliza: PolizaInmueble):
        '''Elimina la póliza de la lista si existe'''
        if poliza in self.__seguros:
            self.__seguros.remove(poliza)

    def existePoliza(self, poliza: PolizaInmueble) -> bool:
        '''Retorna True si existe una póliza con la misma identidad'''
        return poliza in self.__seguros

    def hayPolizas(self) -> bool:
        '''Retorna True si hay pólizas en la lista'''
        return bool(self.__seguros)

    def costoTotal(self) -> float:
        '''Retorna el costo total de las pólizas'''
        return sum(poliza.costoPoliza() for poliza in self.__seguros)

    def esIgual(self, aseguradora: 'Aseguradora') -> bool:
        '''Retorna True si las dos colecciones mantienen referencias a los mismos objetos'''
        return self.__seguros == aseguradora.get_seguros()

    def get_seguros(self):
        '''Retorna una copia de la lista de seguros'''
        return self.__seguros.copy()



