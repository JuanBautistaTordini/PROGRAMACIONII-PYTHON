from clases.Ciudad import Ciudad

'''
Diagrama de clases Hotel:

<<atributo de clases>>
-nombre: str
-estrellas: int
-descrpcion: str
-pension: str
-ciudad: Ciudad

<<metodos de clase>>
+fromDiccionario(string): Hotel

<<metodos de instancia>>
+Hotel(nombre: str, estrellas: int, desc: str, pension: str, ciudad: Ciudad)

+obtenerNombre(): str
+obtenerEstrellas(): int
+toString(): str
+esIgualProf(otro: Hotel): bool
+toDiccionario(): dict

<<enumeration>>
Pension:

DESAYUNO
MEDIA_PENSION
PENSION_COMPLETA
'''

class Hotel:
    nombre = ""
    estrellas = 0
    descripcion = ""
    pension = ""
    ciudad = Ciudad()

    @classmethod
    def fromDiccionario(cls, dic):
        h = Hotel(dic["nombre"], dic["estrellas"], dic["descripcion"], dic["pension"], Ciudad.fromDiccionario(dic["ciudad"]))
        return h

    def __init__(self, nombre, estrellas, desc, pension, ciudad):
        self.nombre = nombre
        self.estrellas = estrellas
        self.descripcion = desc
        self.pension = pension
        self.ciudad = ciudad

    def obtenerNombre(self):
        return self.nombre

    def obtenerEstrellas(self):
        return self.estrellas

    def toString(self):
        return f"{self.nombre} ({self.estrellas} estrellas) - {self.ciudad.obtenerNombre()}"

    def esIgualProf(self, otro):
        return self.nombre == otro.nombre and self.estrellas == otro.estrellas and self.ciudad.esIgualProf(otro.ciudad)

    def toDiccionario(self):
        return {
            "nombre": self.nombre,
            "estrellas": self.estrellas,
            "descripcion": self.descripcion,
            "pension": self.pension,
            "ciudad": self.ciudad.toDiccionario()
        }
