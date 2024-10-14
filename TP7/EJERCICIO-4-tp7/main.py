# main.py

from dispositivo import Dispositivo
from pais import Pais
from cancion import Cancion
from playlist import Playlist
from suscripcion_gratuita import SuscripcionGratuita
from suscripcion_paga import SuscripcionPaga

class Tester:
    def __init__(self):
        self.run_tests()

    def run_tests(self):
        # Crear un país
        pais = Pais("ARG", "Argentina", 4)
        print(f"País creado: {pais.get_nombre()}")

        # Crear dispositivos
        dispositivo1 = Dispositivo(1, "Teléfono", "Móvil")
        dispositivo2 = Dispositivo(2, "Laptop", "Computadora")
        print(f"Dispositivos creados: {dispositivo1.get_nombre()}, {dispositivo2.get_nombre()}")

        # Crear canciones
        cancion1 = Cancion(101, "Canción A", 3, "Pop")
        cancion2 = Cancion(102, "Canción B", 4, "Rock")
        print(f"Canciones creadas: {cancion1.get_nombre()}, {cancion2.get_nombre()}")

        # Crear una playlist
        playlist = Playlist(1, "Mi Playlist")
        playlist.agregarCancion(cancion1)
        playlist.agregarCancion(cancion2)
        print(f"Playlist creada: {playlist.get_nombre()} con canciones: {[c.get_nombre() for c in playlist.get_canciones()]}")

        # Crear suscripciones
        suscriptor_gratuito = SuscripcionGratuita("Juan", "juan@example.com", "123456789", pais, 30, 10)
        suscriptor_pago = SuscripcionPaga("Maria", "maria@example.com", "987654321", pais, 4)

        # Probar reproducción de música
        suscriptor_gratuito.reproducirMusica()
        suscriptor_pago.reproducirMusica()

        # Habilitar dispositivos
        suscriptor_pago.habilitarDispositivo(dispositivo1)
        suscriptor_pago.habilitarDispositivo(dispositivo2)

        # Descargar música
        suscriptor_pago.descargarMusica()

        # Elegir canción
        suscriptor_pago.elegirCancion(cancion1)

if __name__ == "__main__":
    Tester()