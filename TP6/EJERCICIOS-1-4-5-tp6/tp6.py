#De los libros se mantiene el nombre, su autor, editorial, categoria (A, B o C) 

#Socios se mantiene el nombre, fecha de nacimiento y fecha de penalización (si hubiere)

# cuando se realiza el préstamo se almacena al socio, el 
# libro, la fecha en que se realiza el préstamo y la cantidad de días que se autoriza el 
# préstamo.

# Cuando se devuelve el lirbro se almacena fecha y si fué devuelto a tiempo.

# si excede el plazo, la penalización puede ser de 3 dias con un atraso menor a 7 dias
# 5 dias si el atraso es menor a 21 dias
# 10 dias si el atraso es 21 dias o mas

#si el libro tiene categoría A, las penalizaciones se duplican

# Clase Socio:

# ○ el constructor inicializa al socio sin fecha de penalizacion (None) 
# ○ establecerFechaPenalizacion(fechaHasta: Fecha) actualiza el atributo de 
# instancia fechaPenalizacion. 
# ○ la Consulta estaHabilitado(fecha: Fecha) retorna True cuando no tiene 
# fechaPenalizacion o cuando ésta es anterior a la fecha recibida en el 
# parámetro.

#importar clase fecha del archivo tp5.py

# from tp5 import Fecha

# class Libro:
#     def __init__(self, nombre: str, autor: str, editorial: str, categoria: str):
#         self.__nombre = nombre
#         self.__autor = autor
#         self.__editorial = editorial
#         self.__categoria = categoria # A, B, C o D
    
#     def obtenerNombre(self) -> str:
#         return self.nombre

#     def obtenerAutor(self) -> str:
#         return self.autor
    
#     def obtenerEditorial(self) -> str:
#         return self.editorial
    
#     def obtenerCategoria(self) -> str:
#         return self.categoria
    
#     def __str__(self):
#         return f'Libro: {self.nombre}, Autor: {self.autor}, Editorial: {self.editorial}, Categoria: {self.categoria}'

# class Socio:
    
#     def __init__(self, nombre: str, fechaNacimiento: Fecha):
#         self.__nombre = nombre
#         self.__fechaNacimiento = nacimiento
#         self.__fechaPenalizacion = None # inicia sin fecha de penalizacion
    
#     def establecerNombre(self, nombre: str):
#         self.__nombre = nombre
    
#     def establecerFechaNacimiento(self, fechaNacimiento: Fecha):
#         self.__fechaNacimiento = fecha

#     def establecerFechaPenalizacion(self, fechaHasta: Fecha):
#         self.__fechaPenalizacion = fechaHasta
    
#     #Consultas
    
#     def estaHabilitado(self, fecha: Fecha) -> bool:
#         if self.__fechaPenalizacion is None or self.__fechaPenalizacion <= fecha:
#             return True
#         return False
    
#     def obtenerNombre(self):
#         return self.__nombre
    
#     def obtenerFechaNacimiento(self) -> Fecha:
#         return self.__fechaNacimiento
    
#     def obetenerFechaPenalizacion(self) -> Fecha:
#         return self.__fechaPenalizacion
    
#     def __str__(self):
#         #si existe penalizacion mostrar fecha, sino "sin penalizacion"
#         penalizacion = f"Penalización hasta: {self.fechaPenalizacion}" if self.fechaPenalizacion else "Sin penalización"
#         return f'Socio: {self.nombre}, Fecha Nacimiento: {self.fechaNacimiento}, Fecha Penalización: {penalizacion}'

# class Prestamo:
#     def __init__(self, libro: Libro, fechaPrestamo: Fecha, cantDias: int, socio: Socio):
#         self.__libro = libro
#         self.__fechaPrestamo = fechaPrestamo
#         self.__cantDias = cantDias
#         self.__socio = socio
#         self.__fechaDevolucion = None # inicia sin fecha devolucion
        
#     #Comando:
    
#     def establecerFechaDevolucion(self, fechaDev: Fecha):
#         #establecerFechaDevolucion controla si el socio debe 
#         #recibir una penalización, en caso afirmativo se le asigna al socio la fecha de 
#         #penalización.
#         self.fechaDevolucion = fechaDev
#         fechaLimite = self.fechaPrestamo.sumaDias(self.dias)
#         if fechaDev.esAnterior(fechaLimite) == False:  # Si la devolución es posterior a la fecha límite
#             penalizacion_fecha = self.penalizacion()
#             self.socio.establecerPenalizacion(penalizacion_fecha)
    
#     #Consultas:
    
#     def obtenerLibro(self) -> Libro:
#         return self.__libro
    
#     def obtenerFechaPrestamo(self) -> Fecha:
#         return self.__fechaPrestamo
    
#     def obtenerFechaDevolucion(self) -> Fecha:
#         return self.__fechaDevolucion
    
#     def estaAtrasado(self, fecha: Fecha) -> bool:
#         '''retorna verdadero si el 
#         libro no se devolvió y ya debería haberse devuelto de acuerdo a la fecha de 
#         préstamo y la cantidad de días'''
#         fechaLimite = self.fechaPrestamo.sumaDias(self.dias)
#         return self.fechaDevolucion is None and fechaActual.esAnterior(fechaLimite) == False
    
#     def penalizacion(self) -> Fecha:
#         '''retorna la fecha de penalización según la cantidad de días de atraso'''
#         if self.dias <= 7:
#             return self.fechaPrestamo.sumaDias(3)
#         elif self.dias <= 21:
#             return self.fechaPrestamo.sumaDias(5)
#         else:
#             return self.fechaPrestamo.sumaDias(10)
        
# # Clase Tester
# def tester_prestamo():
#     # Crear una fecha de préstamo usando la clase Fecha
#     fecha_prestamo = Fecha(1, 10, 2024)

#     # Crear un libro de categoría A
#     libro = Libro(nombre="El Quijote", autor="Miguel de Cervantes", editorial="Anaya", categoria='A')

#     # Crear un socio
#     socio = Socio(nombre="Juan Pérez", nacimiento=Fecha(17, 5, 1990))

#     # Crear un préstamo con una duración de 10 días
#     prestamo = Prestamo(libro=libro, fechaPrestamo=fecha_prestamo, cantDias=10, socio=socio)

#     # Simular una devolución atrasada por 15 días
#     fecha_devolucion = Fecha(26, 10, 2024)  # 15 días de retraso desde el 1 de octubre
#     prestamo.establecerFechaDevolucion(fecha_devolucion)

#     # Mostrar resultados
#     print(prestamo)
#     print(f"Fecha de penalización para el socio: {socio.obtenerFechaPenalizacion()}")

#     # Caso interactivo para pedir datos al usuario
#     nombre_libro = input("Ingrese el nombre del libro: ")
#     autor_libro = input("Ingrese el autor del libro: ")
#     editorial_libro = input("Ingrese la editorial del libro: ")
#     categoria_libro = input("Ingrese la categoría del libro (A, B, C): ")

#     nuevo_libro = Libro(nombre=nombre_libro, autor=autor_libro, editorial=editorial_libro, categoria=categoria_libro)

#     print(nuevo_libro)


# # Ejecutar tester
# tester_prestamo()



