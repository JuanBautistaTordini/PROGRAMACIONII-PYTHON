# suscripcion.py

# Clase Suscripción

class Suscripcion:
    def __init__(self, nombre, email, telefono, pais):
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono
        self.__pais = pais

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self.__nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if isinstance(email, str) and '@' in email:
            self.__email = email
        else:
            raise ValueError("El email debe ser una dirección válida")

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        if isinstance(telefono, str) and telefono.isdigit():
            self.__telefono = telefono
        else:
            raise ValueError("El teléfono debe ser una cadena de dígitos")

    def get_pais(self):
        return self.__pais

    def set_pais(self, pais):
        if isinstance(pais, str) and pais.strip():
            self.__pais = pais
        else:
            raise ValueError("El país debe ser una cadena no vacía")

    def reproducirMusica(self):
        pass  # Implementar en clases derivadas


