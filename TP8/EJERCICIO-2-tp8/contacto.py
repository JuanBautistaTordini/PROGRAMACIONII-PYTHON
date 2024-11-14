# nombre,
# apellido, teléfono, correo electrónico y dirección, todo en formato string)

'''
Diagrama de Clase contacto:

+--------------------------------+
|           Contacto             |
+--------------------------------+
| -nombre: str                   |
| -apellido: str                 |
| -telefono: str                 |
| -correo_electronico: str       |
| -direccion: str                |
| Metodos:                       |
| +get_nombre(): str             |
| +get_apellido(): str           |
| +get_telefono(): str           |
| +get_correo_electronico(): str |
| +get_direccion(): str          |
| +toDiccionario(): dict         |
| +fromDiccionario(dict): dict   |
+--------------------------------+

'''

import json

class Contacto:
    """
    Clase que representa un contacto con información personal.

    Atributos:
    - nombre (str): El nombre del contacto.
    - apellido (str): El apellido del contacto.
    - telefono (str): El número de teléfono del contacto.
    - correo_electronico (str): El correo electrónico del contacto.
    - direccion (str): La dirección del contacto.
    """

    def __init__(self, nombre: str, apellido: str, telefono: str, correo_electronico: str, direccion: str):
        # validaciones:
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un string.")
        if not isinstance(apellido, str):
            raise ValueError("El apellido debe ser un string.")
        if not isinstance(telefono, str):
            raise ValueError("El teléfono debe ser un string.")
        if not isinstance(correo_electronico, str):
            raise ValueError("El correo electrónico debe ser un string.")
        if not isinstance(direccion, str):
            raise ValueError("La dirección debe ser un string.")
        
        # atributos:
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.direccion = direccion
        
    # Getters
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido    
    
    def get_telefono(self):
        return self.telefono
    
    def get_correo_electronico(self):
        return self.correo_electronico
    
    def get_dereccion(self):
        return self.direccion
    
    # Método serializacion/desealizacion
    
    def toDiccionario(self):
        """
        Convierte el objeto Contacto en un diccionario.

        Returns:
        - dict: Un diccionario con los atributos del contacto.
        """
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
            "correo_electronico": self.correo_electronico,
            "direccion": self.direccion
        }
    
    @staticmethod
    def fromDiccionario(dicc):
        """
        Crea un objeto Contacto a partir de un diccionario.

        Args:
        - dicc (dict): Un diccionario con los atributos del contacto.

        Returns:
        - Contacto: Un objeto Contacto con los atributos del diccionario.
        """
        return Contacto(
            nombre = dicc["nombre"],
            apellido = dicc["apellido"],
            telefono = dicc["telefono"],
            correo_electronico = dicc["correo_electronico"],
            direccion = dicc["direccion"]
        )
    
    def __str__(self):
        return (f'{self.nombre} {self.apellido} - Teléfono: {self.telefono} - Correo electrónico: {self.correo_electronico} - Dirección: {self.direccion}')