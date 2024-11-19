'''
+-------------------------+
|     Socio               |
+-------------------------+
| -DNI: int               |
| -nombre: str            |
| -apellido: str          |
| -mail: str              |
| -fecha_nacimiento: str  |
+-------------------------+
| <<metodos de clas>>     |
| +fromDiccionario(dic:Diccionario): Socio |
| <<metodos de instancia>>|
| +Socio(dni:int, nombre:str, apellido:str, mail:str, fecha_nacimiento:date)|
| <<consultas triviales>> ... |
| <<comandos triviales>> ... |
| +esIgual(otro: Socio): bool |
| +toString(): str |
|+ toDiccionario(): diccionario |
+-------------------------+

'''

from datetime import datetime

class Socio:
    def __init__(self, dni:int, nombre:str, apellido:str, mail:str, fecha_nacimiento:datetime):
        # validaciones:
        if not isinstance(dni, int):
            raise ValueError("El dni debe ser un entero")
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un string")
        if not isinstance(apellido, str):
            raise ValueError("El apellido debe ser un string")
        if not isinstance(mail, str):
            raise ValueError("El mail debe ser un string")
        if not isinstance(fecha_nacimiento, str):
            raise ValueError("La fecha de nacimiento debe ser un string")
        
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.fecha_nacimiento = fecha_nacimiento
    
    # <<metodos de instancia>>
    @classmethod
    def fromDiccionario(cls, dicc:dict):
        return cls(
            dicc['dni'],
            dicc['nombre'],
            dicc['apellido'],
            dicc['mail'],
            dicc['fecha_nacimiento']
        )
    
    # <<consultas triviales>>
    def getDni(self):
        return self.dni
    
    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido
    
    def getMail(self):
        return self.mail
    
    def getFechaNacimiento(self):
        return self.fecha_nacimiento
    
    # <<comandos triviales>>
    def setDni(self, dni:int):
        if not isinstance(dni, int):
            raise ValueError("El dni debe ser un entero")
        self.dni = dni
        
    def setNombre(self, nombre:str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un string")
        self.nombre = nombre
    
    def setApellido(self, apellido:str):
        if not isinstance(apellido, str):
            raise ValueError("El apellido debe ser un string")
        self.apellido = apellido
    
    def setMail(self, mail:str):
        if not isinstance(mail, str):
            raise ValueError("El mail debe ser un string")
        self.mail = mail
    
    def setFechaNacimiento(self, fecha_nacimiento:datetime):
        if not isinstance(fecha_nacimiento, str):
            raise ValueError("La fecha de nacimiento debe ser un string")
        self.fecha_nacimiento = fecha_nacimiento
    
    # <<metodos de instancia>>
    def esIgual(self, otro):
        return self.dni == otro.dni
    
    def __str__(self):
        return f"Socio: {self.dni}, {self.nombre}, {self.apellido}, {self.mail}, {self.fecha_nacimiento}"
    
    def toDiccionario(self):
        return {
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'mail': self.mail,
            'fecha_nacimiento': self.fecha_nacimiento
        }

    
        