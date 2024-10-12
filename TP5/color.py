class Color:
    # Definimos las constantes de color como atributos de clase
    ROJO = (255, 0, 0)
    VERDE = (0, 255, 0)
    AZUL = (0, 0, 255)

    def __init__(self, rojo=255, verde=255, azul=255):
        self._rojo = self._validar_color(rojo)
        self._verde = self._validar_color(verde)
        self._azul = self._validar_color(azul)

    def _validar_color(self, valor):
        # Método auxiliar para validar que el color esté entre 0 y 255
        return max(0, min(valor, 255))

    # Comandos para modificar los valores de color
    def variar(self, valor):
        self.variarRojo(valor)
        self.variarVerde(valor)
        self.variarAzul(valor)

    def variarRojo(self, valor):
        self._rojo = self._validar_color(self._rojo + valor)

    def variarVerde(self, valor):
        self._verde = self._validar_color(self._verde + valor)

    def variarAzul(self, valor):
        self._azul = self._validar_color(self._azul + valor)

    def establecerRojo(self, valor):
        self._rojo = self._validar_color(valor)

    def establecerVerde(self, valor):
        self._verde = self._validar_color(valor)

    def establecerAzul(self, valor):
        self._azul = self._validar_color(valor)

    def copiar(self, otroColor):
        self._rojo = otroColor._rojo
        self._verde = otroColor._verde
        self._azul = otroColor._azul

    # Consultas para obtener los valores de color
    def obtenerRojo(self):
        return self._rojo

    def obtenerVerde(self):
        return self._verde

    def obtenerAzul(self):
        return self._azul

    def esRojo(self):
        return self._rojo == 255 and self._verde == 0 and self._azul == 0

    def esGris(self):
        return self._rojo == self._verde == self._azul

    def esNegro(self):
        return self._rojo == 0 and self._verde == 0 and self._azul == 0

    def complemento(self):
        return Color(255 - self._rojo, 255 - self._verde, 255 - self._azul)

    def esIgualQue(self, otroColor):
        return (self._rojo == otroColor._rojo and
                self._verde == otroColor._verde and
                self._azul == otroColor._azul)

    def clonar(self):
        return Color(self._rojo, self._verde, self._azul)
