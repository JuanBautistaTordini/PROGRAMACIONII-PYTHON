'''
+---------------------+
| Clase: RepoSocios   |
+---------------------+
| -socios: list<Socio>|
+---------------------+
| +RepositorioSocio() |
| -cargarTodos()     |
| -guardarTodos()    |
| +obtenerTodos()     |
| +existe(socios: Socio): bool|
| +existeDNI(dni: int): bool|
| +agregar(nuevoSocio: Socio)|
| modificarPorDNI(dni: int, nombre: str, apellido: str, mail: str, fecha_nacimiento: date)|
| +eliminarPorDNI(dni: int)|
+---------------------+
'''

from modelos.entidades.classSocio import Socio
from datetime import datetime
import json

class RepoSocios:
    def __init__(self):
        self.socios = []
        self.cargarTodos()
    
    def cargarTodos(self):
        try:
            with open('./datos/socios.json', 'r', encoding = 'utf-8') as archivo:
                socios = json.load(archivo)
                for socio in socios:
                    self.socios.append(Socio.fromDiccionario(socio))
        except FileNotFoundError:
            return []
        
    def guardarTodos(self):
        try: 
            with open('./datos/socios.json', 'w', encoding = 'utf-8') as archivo:
                socios = []
                for socio in self.socios:
                    socios.append(socio.toDiccionario())
                json.dump(socios, archivo)
        except FileNotFoundError:
            return []
    
    def obtenerTodos(self):
        return self.socios
    
    def existe(self, socio: Socio):
        return socio in self.socios
    
    def existeDNI(self, dni: int):
        for socio in self.socios:
            if socio.getDni() == dni:
                return True
        return False

    def agregar(self, nuevoSocio: Socio):
        if not self.existe(nuevoSocio):
            self.socios.append(nuevoSocio)
            self.guardarTodos()
        else:
            raise ValueError("El socio ya existe")
    
    def modificarPorDNI(self, dni: int, nombre: str, apellido: str, mail: str, fecha_nacimiento: datetime):
        for socio in self.socios:
            if socio.getDni() == dni:
                socio.nombre = nombre
                socio.apellido = apellido
                socio.mail = mail
                socio.fecha_nacimiento = fecha_nacimiento
                self.guardarTodos()
                return
        raise ValueError("El socio no existe")
    
    def eliminarPorDNI(self, dni: int):
        for socio in self.socios:
            if socio.getDni() == dni:
                self.socios.remove(socio)
                self.guardarTodos()
                return
        raise ValueError("El socio no existe")
    
    def __str__(self):
        return f"Socios: {self.socios}"
            
        
        