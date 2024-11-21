'''
+--------------------------------+
|      repoPrestamo.py           |
+--------------------------------+
| - prestamos: list<Prestamo>    |
+--------------------------------+
| + RepositorioPrestamo()        |
| + cargarTodos()                |
| + guardarTodos()               |
| + obtenerTodos(): list<Prestamo>|
| + estaDevuelto(prestamo: Prestamo) -> bool|
| + agregar(nuevoPrestamo: Prestamo)|
| + existe(socio_dni: int, libro_isbn: int, fecha_retiro: date) -> bool|
| + obtenerPrestamo(socio_dni: int, libro_isbn: int, fecha_retiro: date) -> Prestamo|
| + modficarPorID(id: int, socio_dni: int, libro_isbn: int, fecha_retiro: date, cant_dias: int, fecha_devolucion: date)|
| + eliminarPorID(id: int)|
| + cantidadLibrosSinDevolver(isbn: int) -> int|
+--------------------------------+

OBSERVACIONES:
- existe(socio_dni: int, libro_isbn: int, fecha_retiro: date) devuelve True si existe un prestamo en la lista con la combinacion de valores recibidos por parametro.

-obtenerPrestamo(socio_dni: int, libro_isbn: int, fecha_retiro: date) -> Prestamo devuelve el prestamo que coincida con los valores recibidos por parametro, si no existe retorna None.

- cantidadLibrosSinDevolver(isbn: int) -> int retorna la cantidad de prestamos de libros que tienen el ISBN recibido por parametro y que aun no ha sido devueltos.


'''

from modelos.entidades.classPrestamo import Prestamo

class RepositorioPrestamo:
    def __init__(self):
        self.prestamos = []
        self.cargarTodos()
        
    def cargarTodos(self):
        try:
            with open('datos/prestamos.json', 'r', encoding = 'utf-8') as archivo:
                prestamos = json.load(archivo)
                for prestamo in prestamos:
                    self.prestamos.append(Prestamo.fromDiccionario(prestamo))
        except FileNotFoundError:
            return []
    
    def guardarTodos(self):
        try:
            with open('datos/prestamos.json', 'w', encoding = 'utf-8') as archivo:
                prestamos = []
                for prestamo in self.prestamos:
                    prestamos.append(prestamo.toDiccionario())
                json.dump(prestamos, archivo)
        except FileNotFoundError:
            return []
    
    def obtenerTodos(self):
        return self.prestamos
    
    def estaDevuelto(self, prestamo: Prestamo) -> bool:
        return prestamo.fecha_devolucion is not None
    
    def agregar(self, nuevoPrestamo: Prestamo):
        try: 
            if not self.existe(nuevoPrestamo.socio_dni, nuevoPrestamo.libro_isbn, nuevoPrestamo.fecha_retiro):
                self.prestamos.append(nuevoPrestamo)
                self.guardarTodos()
            else:
                raise ValueError("El prestamo ya existe.")
        except FileNotFoundError:
            return raise ValueError("Error al guardar los datos.")
        
    '''
    def existe(socio_dni: int, libro_isbn: int, fecha_retiro: date) 
    devuelve True si existe un prestamo en la lista con la 
    combinacion de valores recibidos por parametro.
    '''
    def existe(self, socio_dni: int, libro_isbn: int, fecha_retiro: datetime) -> bool:
        try:
            for prestamo in self.prestamos:
                if prestamo.socio_dni == socio_dni and prestamo.libro_isbn == libro_isbn and prestamo.fecha_retiro == fecha_retiro:
                    return True
            return False
        except FileNotFoundError:
            return raise ValueError("Error al comprobar la existencia del prestamo.")
        
    '''
    -obtenerPrestamo(socio_dni: int, libro_isbn: int, fecha_retiro: date) -> Prestamo 
    devuelve el prestamo que coincida con los valores recibidos por parametro, 
    si no existe retorna None.
    '''
    
    def obtenerPrestamo(self, socio_dni: int, libro_isbn: int, fecha_retiro: datetime) -> Prestamo:
        try:
            for prestamo in self.prestamos:
                if prestamo.socio_dni == socio_dni and prestamo.libro_isbn == libro_isbn and prestamo.fecha_retiro == fecha_retiro:
                    return prestamo
            return None
        except FileNotFoundError:
            return raise ValueError("Error al obtener el prestamo.")
    
    def modificarPorID(self, id: int, socio_dni: int, libro_isbn: int, fecha_retiro: datetime, cant_dias: int, fecha_devolucion: datetime):
        try:
            for prestamo in self.prestamos:
                if prestamo.id == id:
                    prestamo.socio_dni = socio_dni
                    prestamo.libro_isbn = libro_isbn
                    prestamo.fecha_retiro = fecha_retiro
                    prestamo.cant_dias = cant_dias
                    prestamo.fecha_devolucion = fecha_devolucion
                    self.guardarTodos()
                    return
            raise ValueError("El prestamo no existe.")
        except FileNotFoundError:
            return raise ValueError("Error al modificar el prestamo.")
    
    def eliminarPorID(self, id: int):
        try:
            for prestamo in self.prestamos:
                if prestamo.id == id:
                    self.prestamos.remove(prestamo)
                    self.guardarTodos()
                    return
            raise ValueError("El prestamo no existe.")
        except FileNotFoundError:
            return raise ValueError("Error al eliminar el prestamo.")
    
    '''
    - cantidadLibrosSinDevolver(isbn: int) -> int retorna la cantidad de 
    prestamos de libros que tienen el ISBN recibido por parametro y que 
    aun no ha sido devueltos.
    '''
    
    def cantidadLibrosSinDevolver(self, isbn: int) -> int:
        try:
            cantidad = 0
            for prestamo in self.prestamos:
                if prestamo.libro_isbn == isbn and not self.estaDevuelto(prestamo):
                    cantidad += 1
            return cantidad
        except FileNotFoundError:
            return raise ValueError("Error al obtener la cantidad de libros sin devolver.")

    