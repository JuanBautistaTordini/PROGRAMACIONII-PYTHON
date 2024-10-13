# Clase Organizador:

#     Atributos:
#         nombre: Nombre del organizador (string).
#         email: Dirección de correo electrónico (string).
#         especialidad: Especialidad del organizador (string).
#         eventos: Lista de eventos que el organizador está a cargo.
        
#     Métodos:
#     asignar_evento(evento): Asigna un evento al organizador.

# Evento: Cada evento tiene un nombre, una fecha y una descripción. Los eventos 
# pueden tener múltiples participantes y un organizador asignado. 

# Participante: Cada participante tiene un nombre, una dirección de correo electrónico 
# y un número de teléfono. Los participantes pueden registrarse en uno o más 
# eventos. 

# Organizador: Cada organizador tiene un nombre, una dirección de correo electrónico 
# y una especialidad (por ejemplo, planificación de eventos, catering, músico, DJ, etc.). 
# Cada organizador puede estar a cargo de uno o más eventos. 

# B. Implementa las clases en python 

class Organizador:
    def __init__(self, nombre: str, email: str, especialidad: str):
        #validaciones:
        if not isinstance(especialidad, str):
            raise ValueError("especialidad no es una cadena de caracteres")
        if not isinstance(email, str):
            raise ValueError("email no es una cadena de caracteres")
        if not isinstance(nombre, str):
            raise ValueError("nombre no es una cadena de caracteres")

        #asignaciones:
        self.__nombre = nombre
        self.__email = email
        self.__especialidad = especialidad
        self.__eventos = []

    #Geters y setters

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_especialidad(self):
        return self.__especialidad

    def set_especialidad(self, especialidad):
        self.__especialidad = especialidad

    def get_eventos(self):
        return self.__eventos
    
    def set_eventos(self):
        return self.__eventos

    def asignar_evento(self, evento):
        self.__eventos.append(evento)
    
    def __str__(self):
        return (f"Organizador: {self.__nombre}\n"
                f"Email: {self.__email}\n"
                f"Especialidad: {self.__especialidad}\n"
                f"Eventos: {self.__eventos}")
    