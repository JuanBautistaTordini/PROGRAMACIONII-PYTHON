# suscripcion_gratuita.py

# constructo: nombre, email, telefono, pais, tiempoSinPublicidad, tiempoReproducido
# import suscripcion
from suscripcion import Suscripcion

# Clase SuscripcionGratuita
class SuscripcionGratuita(Suscripcion):
    def __init__(self, nombre, email, telefono, pais, tiempoSinPublicidad, tiempoReproducido):
        super().__init__(nombre, email, telefono, pais)
        self.__tiempoSinPublicidad = tiempoSinPublicidad
        self.__tiempoReproducido = tiempoReproducido
        
    def get_tiempoSinPublicidad(self):
        return self.__tiempoSinPublicidad

    def set_tiempoSinPublicidad(self, tiempoSinPublicidad):
        if isinstance(tiempoSinPublicidad, int) and tiempoSinPublicidad >= 0:
            self.__tiempoSinPublicidad = tiempoSinPublicidad
        else:
            raise ValueError("El tiempo sin publicidad debe ser un número entero no negativo.")

    def get_tiempoReproducido(self):
        return self.__tiempoReproducido

    def set_tiempoReproducido(self, tiempoReproducido):
        if isinstance(tiempoReproducido, int) and tiempoReproducido >= 0:
            self.__tiempoReproducido = tiempoReproducido
        else:
            raise ValueError("El tiempo reproducido debe ser un número entero no negativo.")

    def reproducirMusica(self):
        print("Reproduciendo música con publicidad.")

    def interrumpirConPublicidad(self):
        print("Interrumpiendo con publicidad.")
    
