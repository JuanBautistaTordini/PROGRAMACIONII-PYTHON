# main.py

'''En un sistema de administración de personal se tienen tres categorías: 
administrativos, programadores y personal de mantenimiento. Cada uno de ellos 
posee nombre, apellido y DNI. Los administrativos tienen número de legajo y 
posición. Los programadores tienen número de legajo y proyecto al que son 
asignados. El personal de mantenimiento tiene legajo, y el nombre del área a la que 
son asignados.  
a. Realice un diagrama UML completo que represente la jerarquía de clases. 
b. Implementar las clases en python.'''

from administrativo import Administrativo
from programador import Programador
from mantenimiento import Mantenimiento

if __name__ == "__main__":
    # Crear instancias de cada clase
    admin = Administrativo("Juan", "Pérez", "12345678", "A001", "Gerente")
    programador = Programador("Ana", "Gómez", "87654321", "P001", "Proyecto X")
    mantenimiento = Mantenimiento("Luis", "Martínez", "11223344", "M001", "Electromecánica")

    # Mostrar detalles de cada instancia
    print(admin)
    print(programador)
    print(mantenimiento)