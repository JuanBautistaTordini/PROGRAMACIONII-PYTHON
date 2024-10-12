# Clase Participante:

#     Atributos:
#         nombre: Nombre del participante (string).
#         email: Dirección de correo electrónico (string).
#         telefono: Número de teléfono (string).
#         eventos: Lista de eventos en los que está registrado el participante.
        
#     Métodos:
#     registrarse_evento(evento: Evento): Registra al participante en un evento.

# Evento: Cada evento tiene un nombre, una fecha y una descripción. Los eventos 
# pueden tener múltiples participantes y un organizador asignado. 

# Participante: Cada participante tiene un nombre, una dirección de correo electrónico 
# y un número de teléfono. Los participantes pueden registrarse en uno o más 
# eventos. 

# Organizador: Cada organizador tiene un nombre, una dirección de correo electrónico 
# y una especialidad (por ejemplo, planificación de eventos, catering, músico, DJ, etc.). 
# Cada organizador puede estar a cargo de uno o más eventos. 

# B. Implementa las clases en python 

#importar clase evento:

from evento import Evento  # Asegúrate de que este nombre de archivo es correcto

class Participante:
    def __init__(self, nombre: str, email: str, telefono: str):
        # Validaciones
        if not nombre:
            raise ValueError("El nombre del participante no puede estar vacío.")
        if not email:
            raise ValueError("El email del participante no puede estar vacío.")
        if not telefono:
            raise ValueError("El teléfono del participante no puede estar vacío.")
        
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono
        self.__eventos = []
    
    # Getters y setters
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        if not nombre:
            raise ValueError("El nombre del participante no puede estar vacío.")
        self.__nombre = nombre
    
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        if not email:
            raise ValueError("El email del participante no puede estar vacío.")
        self.__email = email
    
    def get_telefono(self):
        return self.__telefono
    
    def set_telefono(self, telefono):
        if not telefono:
            raise ValueError("El teléfono del participante no puede estar vacío.")
        self.__telefono = telefono
    
    def get_eventos(self):
        return self.__eventos
    
    def registrarse_evento(self, evento: Evento):
        if not isinstance(evento, Evento):
            raise TypeError("El evento debe ser una instancia de la clase Evento.")
        self.__eventos.append(evento)

    def __str__(self):
        eventos_nombres = [evento.get_nombre() for evento in self.__eventos]
        return (
            f"Participante: {self.__nombre}\n"
            f"Email: {self.__email}\n"
            f"Teléfono: {self.__telefono}\n"
            f"Eventos: {', '.join(eventos_nombres) if eventos_nombres else 'Ninguno'}"
        )

# Tester
if __name__ == "__main__":
    # Crear participante
    participante = Participante("Juan Pérez", "juan@example.com", "123456789")

    # Crear evento
    evento = Evento("Festival de Muñecos", "2023-06-01", "Concierto de Muñecos")

    # Registrar participante en evento
    participante.registrarse_evento(evento)

    # Imprimir datos del participante
    print(participante)

    # Imprimir datos del evento
    print(evento)

    