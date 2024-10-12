# A. Diseño del Diagrama UML
    # Clases Principales:

        # Participante

            # Atributos:
            # nombre: str
            # edad: int
            # nacionalidad: str
            # disciplinas: List[Disciplina] (relación de muchos a muchos con Disciplina)
            
            # Métodos:
            # __init__(nombre, edad, nacionalidad)
            # agregar_disciplina(disciplina: Disciplina)
            # __str__(): para representar al participante en formato legible.
            
        # Disciplina

            # Atributos:
            # nombre: str
            # descripcion: str
            # participantes: List[Participante] (relación de muchos a muchos con Participante)
            
            # Métodos:
            # __init__(nombre, descripcion)
            # agregar_participante(participante: Participante)
            # __str__(): para representar la disciplina en formato legible.
        
    # Relaciones:
    
        # Un Participante puede competir en varias Disciplinas.
        # Una Disciplina puede tener varios Participantes.
        
# B. Implementar las clases en python:

# Participante:

class Participante:
    def __init__(self, nombre: str, edad: int, nacionalidad: str):
        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad
        self.__disciplinas = []
    
    def agregar_disciplina(self, disciplina: 'Disciplina'):
        if disciplina not in self.__disciplinas:
            self.__disciplinas.append(disciplina)
    
    def __str__(self):
        return f'Participante: {self.__nombre}, {self.__edad} años, {self.__nacionalidad}'

# Disciplina:

class Disciplina:
    def __init__(self, nombre: str, descripcion: str):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__participantes = []
    
    def agregar_participante(self, participante: 'Participante'):
        if participante not in self.__participantes:
            self.__participantes.append(participante)
    
    def __str__(self):
        return f'Disciplina: {self.__nombre}, {self.__descripcion}'

# C.  Desarrollar una clase tester que pida al usuario los datos para registrar las 
# disciplinas, y los datos de los participantes. Luego debe permitir al usuario 
# ver todos los participantes inscriptos en una disciplina y las disciplinas en las 
# que participa cada competidor

# Clase Tester:

class Tester:
    def __init__(self):
        self.__disciplinas = []
        self.__participantes = []
    
    def registrar_disciplina(self):
        nombre = input('Ingrese el nombre de la disciplina: ')
        descripcion = input('Ingrese una descripción de la disciplina: ')
        disciplina = Disciplina(nombre, descripcion)
        self.__disciplinas.append(disciplina)
    
    def registrar_participante(self):
        nombre = input('Ingrese el nombre del participante: ')
        edad = int(input('Ingrese la edad del participante: '))
        nacionalidad = input('Ingrese la nacionalidad del participante: ')
        participante = Participante(nombre, edad, nacionalidad)
        self.__participantes.append(participante)
    
    def ver_participantes_disciplina(self):
        if not self.__disciplinas:
            print('No hay disciplinas registradas.')
            return
        
        nombre_disciplina = input('Ingrese el nombre de la disciplina: ')
        for disciplina in self.__disciplinas:
            if disciplina.nombre == nombre_disciplina:
                print(f'Participantes en la disciplina {disciplina.nombre}:')
                for participante in disciplina.participantes:
                    print(participante)
                return
        
        print('Disciplina no encontrada.')
    
    def ver_disciplinas_participante(self):
        if not self.__participantes:
            print('No hay participantes registrados.')
            return
        
        nombre_participante = input('Ingrese el nombre del participante: ')
        for participante in self.__participantes:
            if participante.nombre == nombre_participante:
                print(f'Disciplinas en las que participa el participante {participante.nombre}:')
                for disciplina in participante.disciplinas:
                    print(disciplina)
                return
        
        print('Participante no encontrado.')
    
    def menu(self):
        while True:
            print('\nMenú:')
            print('1. Registrar disciplina')
            print('2. Registrar participante')
            print('3. Ver participantes en una disciplina')
            print('4. Ver disciplinas en las que participa un participante')
            print('5. Salir')
            
            opcion = int(input('Ingrese una opción: '))
            
            if opcion == 1:
                self.registrar_disciplina()
            elif opcion == 2:
                self.registrar_participante()
            elif opcion == 3:
                self.ver_participantes_disciplina()
            elif opcion == 4:
                self.ver_disciplinas_participante()
            elif opcion == 5:
                print('Saliendo...')
                break
            else:
                print('Opción inválida.')
    
    def run(self):
        self.menu()

# Instanciar la clase Tester y ejecutar el programa:

tester = Tester()
tester.run()