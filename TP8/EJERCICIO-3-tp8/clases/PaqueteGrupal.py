'''
Diagrama de clases:

<<atributo de clases>>
ultimoId: int

<<atributo de instancia>>
-id: int
-fechaSalida: Fecha
-fechaVuelta: Fecha
-descripcion: str
-tipo: TipoViaje
-transporte: Transporte
-precio: float
-ciudad: Ciudad
-hotel: Hotel
-cupoMaximo: int
-cupoActual: int

<<metodo de clases>>

+obtenerNuevoId(): int
+fromDiccionario(dic: Diccionario): PaqueteGrupal

<<metodo de instancia>>
+PaqueteGrupal(ciudad: Ciudad, hotel: Hotel, fecha_salidad:str, fecha_vuelta:str, descripcion:str, tipo:TipoViaje, transporte:Transporte, precio:float, cupo_maximo:int)

<<consultas y comandos triviales>> ...

+capacidadDisponible(): int
+inscribirPasajeros(cantidad:int)
+__str__(): str
+esIgualProf(paq:PaqueteGrupal): bool
+toDiccionario(): dict

OBSERVACIONES:
el metodo de clase obetenerNuevoId():int se utiliza para 
obtener un ID unico para cada nueva instancia de
PaqueteGrupal. Cada vez que se llama al metodo.
ultimo_is se incrementa y se asigna como valor de retorno 
del metodo
'''
from date import Fecha

class PaqueteGrupal:
    ultimoId = 0 # atributo de clase 

    def __init__(self, ciudad, hotel, fecha_salida, fecha_vuelta, descripcion, tipo, transporte, precio, cupo_maximo):
        # validaciones
        if not isinstance(ciudad, Ciudad):
            raise ValueError("ciudad debe ser una instancia de Ciudad")
        if not isinstance(hotel, Hotel):
            raise ValueError("hotel debe ser una instancia de Hotel")
        if not isinstance(fecha_salida, Fecha):
            raise ValueError("fecha_salida debe ser una instancia de Fecha")
        if not isinstance(fecha_vuelta, Fecha):
            raise ValueError("fecha_vuelta debe ser una instancia de Fecha")
        if not isinstance(descripcion, str):
            raise ValueError("descripcion debe ser una instancia de str")
        if not isinstance(tipo, TipoViaje):
            raise ValueError("tipo debe ser una instancia de TipoViaje")
        if not isinstance(transporte, Transporte):
            raise ValueError("transporte debe ser una instancia de Transporte")
        if not isinstance(precio, float):
            raise ValueError("precio debe ser una instancia de float")
        if not isinstance(cupo_maximo, int):
            raise ValueError("cupo_maximo debe ser una instancia de int")
        if cupo_maximo <= 0:
            raise ValueError("cupo_maximo debe ser mayor a 0")
        if precio <= 0:
            raise ValueError("precio debe ser mayor a 0")
        if fecha_salida > fecha_vuelta:
            raise ValueError("fecha_salida debe ser menor a fecha_vuelta")
        
        # asignaciones
        self.id = PaqueteGrupal.obtenerNuevoId()
        self.fechaSalida = fecha_salida
        self.fechaVuelta = fecha_vuelta
        self.descripcion = descripcion
        self.tipo = tipo
        self.transporte = transporte
        self.precio = precio
        self.ciudad = ciudad
        self.hotel = hotel
        self.cupoMaximo = cupo_maximo
        self.cupoActual = 0

    @classmethod
    def obtenerNuevoId(cls):
        cls.ultimoId += 1
        return cls.ultimoId

    @classmethod
    def fromDiccionario(cls, dic):
        return cls(
            dic['ciudad'],
            dic['hotel'],
            dic['fecha_salida'],
            dic['fecha_vuelta'],
            dic['descripcion'],
            dic['tipo'],
            dic['transporte'],
            dic['precio'],
            dic['cupo_maximo']
        )

    def capacidadDisponible(self):
        return self.cupoMaximo - self.cupoActual

    def inscribirPasajeros(self, cantidad):
        if self.cupoActual + cantidad <= self.cupoMaximo:
            self.cupoActual += cantidad
        else:
            raise ValueError("No hay suficiente capacidad disponible")

    def __str__(self):
        return f"PaqueteGrupal(id={self.id}, ciudad={self.ciudad}, hotel={self.hotel}, fechaSalida={self.fechaSalida}, fechaVuelta={self.fechaVuelta}, descripcion={self.descripcion}, tipo={self.tipo}, transporte={self.transporte}, precio={self.precio}, cupoMaximo={self.cupoMaximo}, cupoActual={self.cupoActual})"

    def esIgualProf(self, paq):
        return self.id == paq.id

    @staticmethod
    def toDiccionario(self):
        return {
            'id': self.id,
            'ciudad': self.ciudad,
            'hotel': self.hotel,
            'fecha_salida': self.fechaSalida,
            'fecha_vuelta': self.fechaVuelta,
            'descripcion': self.descripcion,
            'tipo': self.tipo,
            'transporte': self.transporte,
            'precio': self.precio,
            'cupo_maximo': self.cupoMaximo,
            'cupo_actual': self.cupoActual
        }
    