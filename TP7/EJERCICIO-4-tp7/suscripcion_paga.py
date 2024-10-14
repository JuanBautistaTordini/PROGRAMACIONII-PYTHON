# suscripcion_paga.py

from suscripcion import Suscripcion

class SuscripcionPaga(Suscripcion):
    def __init__(self, nombre, email, telefono, pais, maxDispositivos):
        super().__init__(nombre, email, telefono, pais)
        self.__maxDispositivos = maxDispositivos
        self.__dispositivos = []

    def get_maxDispositivos(self):
        return self.__maxDispositivos

    def set_maxDispositivos(self, maxDispositivos):
        if isinstance(maxDispositivos, int) and maxDispositivos > 0:
            self.__maxDispositivos = maxDispositivos
        else:
            raise ValueError("El número máximo de dispositivos debe ser un entero positivo.")

    def get_dispositivos(self):
        return self.__dispositivos.copy()

    def reproducirMusica(self):
        print("Reproduciendo música sin publicidad.")

    def descargarMusica(self):
        print("Descargando música.")

    def elegirCancion(self, cancion):
        print(f"Eligiendo canción: {cancion.get_nombre()}")  # Cambiado aquí

    def habilitarDispositivo(self, dispositivo):
        if len(self.__dispositivos) < self.__maxDispositivos:
            self.__dispositivos.append(dispositivo)
            print(f"Dispositivo {dispositivo.get_nombre()} habilitado.")  # Cambiado aquí
        else:
            print("Límite de dispositivos alcanzado.")