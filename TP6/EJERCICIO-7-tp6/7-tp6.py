# 7) Un refugio de animales nos pide diseñar un sistema simple para gestionar las 
# mascotas en el refugio. El sistema permitirá registrar mascotas y sus cuidadores, así 
# como asignar y gestionar el cuidado de las mascotas. 
 
# Mascota: Cada mascota tiene un nombre, una especie (por ejemplo, perro, gato), 
# una edad y una descripción. Las mascotas pueden ser asignadas a un cuidador. 
# Cuidador: Cada cuidador tiene un nombre, una dirección y un número de teléfono. 
# Los cuidadores pueden ser asignados a una o más mascotas. 
 
# A. Crea un diagrama de clases que incluya dos clases principales: Mascota y 
# Cuidador. 

# La clase Mascota debe tener los atributos: nombre, especie, edad, 
# descripción. 

# La clase Cuidador debe tener los atributos: nombre, dirección, teléfono y un 
# método para asignar mascotas. 

# B. Implementar las clases con python

# Diagrama de Clases
#     1. Clase Mascota:
#         Atributos:
#             nombre: El nombre de la mascota (string).
#             especie: La especie de la mascota (string), por ejemplo, perro, gato.
#             edad: La edad de la mascota (entero).
#             descripcion: Una breve descripción de la mascota (string).
#             cuidador: Una referencia al cuidador asignado (inicialmente None).

#     2. Clase Cuidador:
#         Atributos:
#             nombre: El nombre del cuidador (string).
#             direccion: La dirección del cuidador (string).
#             telefono: El número de teléfono del cuidador (string).
#             mascotas: Una lista de mascotas asignadas al cuidador.

#         Método:
#         asignar_mascota(mascota): Asigna una mascota al cuidador y actualiza la referencia del cuidador en la mascota.

# Implementación en Python

class Mascota:
    
    def __init__(self,nombre:str,especie:str,edad:int,descripcion:str):
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
        self.__descripcion = descripcion
        self.__cuidador=None
        
    
    def esatblecerNombre(self,nombre:str):
        if not isinstance(nombre,str):
            raise ValueError("El nombre debe ser una cadena de caracteres.")
        self.__nombre = nombre
        
    def establecerEspecie(self,especie:str):
        if not isinstance(especie,str):
            raise ValueError("El nombre de la especie debe ser una cadena de caracteres.")
        self.__especie = especie
        
    def establecerEdad(self,edad:int):
        if not isinstance(edad,int):
            raise ValueError("la edad debe ser un numero")
        self.__edad = edad
        
    def establecerDescripcion(self,descripcion:str):
        if not isinstance(descripcion,str):
            raise ValueError("El nombre debe ser una cadena de caracteres.")
        self.__descripcion = descripcion
        
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerEspecie(self)->str:
        return self.__especie
    
    def obtenerEdad(self)->int:
        return self.__edad
    
    def obtenerDescripcion(self)->str:
        return self.__descripcion
    
    def asignarCuidador(self,cuidador:"Cuidador"):
        self.__cuidador = cuidador
        cuidador.agregarMascota(self)
    
    def conocerCuidador(self):
        return self.__cuidador
    
    def __str__(self):
        return f"nombre={self.__nombre}, especie={self.__especie}, edad={self.__edad}, descripcion={self.__descripcion}"


class Cuidador:
    def __init__(self, nombre: str, direccion: str, telefono: str):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__mascotas = []  # Lista de mascotas asignadas

    def agregarMascota(self,mascota:"Mascota"):
        self.__mascotas.append(mascota)

    def saberMascotas(self):
        return [str(mascota) for mascota in self.__mascotas]

    def __str__(self):
        return f"Cuidador(nombre={self.__nombre}, direccion={self.__direccion}, telefono={self.__telefono})"

# Test

if __name__ == "__main__":
    # Crear cuidadores
    cuidador1 = Cuidador("Juan Perez", "Calle Falsa 123", "123456789")
    cuidador2 = Cuidador("Maria Lopez", "Avenida Siempre Viva 742", "987654321")
    
    # Crear mascotas
    mascota1 = Mascota("Rex", "Perro", 5, "Perro guardián y cariñoso.")
    mascota2 = Mascota("Miau", "Gato", 3, "Gato juguetón y curioso.")
    
    # Asignar mascotas a cuidadores
    mascota1.asignarCuidador(cuidador1)
    mascota2.asignarCuidador(cuidador2)
    
    # Mostrar información
    print(cuidador1)
    print(f"Mascotas de {cuidador1.saberMascotas()}")
    
    print(cuidador2)
    print(f"Mascotas de {cuidador2.saberMascotas()}")
