from color import Color

class Borde:
    ''''
    Clase Borde:
    Atributos de instancia:
    grosor: entero
    color: Color
    
    Constructor:
    Borde(grosor:int, color: Color)
    
    Comandos: 
    coparValores(borde: Borde)
    
    consultas:
    obtenerGrosor(self) -> int
    obtenerColor(self) -> Color
    clonar(self) -> Borde
    esIgualQue(borde: Borde) -> bool
    
    "copiarValores(), clonar() y esIgualQue() superficial"
    '''
    #CONSTRUCTOR
    def __init__(self, grosor: int, color: Color):
        self.__grosor = grosor
        self.__color = color
    
    #COMANDOS
    def copiarValores(self, borde: 'Borde'):
        self.__grosor = borde.__grosor
        self.__color = borde.__color
    
    #CONSULTAS
    def obtenerGrosor(self) -> int:
        return self.__grosor
    
    def obtenerColor(self) -> Color:
        return self.__color
    
    def clonar(self) -> 'Borde':
        return Borde(self.__grosor, self.__color)
    
    def esIgualQue(self, borde: 'Borde') -> bool:
        return self.__grosor == borde.__grosor and self.__color == borde.__color
    
    #SOBRECARGA DE MÉTODOS
    def __str__(self):
        return f'Grosor: {self.__grosor}, Color: {self.__color}'

#Tester de las funciones:

def test_borde():
    # Crear colores
    rojo = Color(255, 0, 0)
    azul = Color(0, 0, 255)
    amarillo = Color(255, 255, 0)
    
    # Crear bordes
    borde_rojo = Borde(5, rojo)
    borde_azul = Borde(3, azul)
    borde_amarillo = Borde(7, amarillo)
    
    # Mostrar bordes
    print(borde_rojo)
    print(borde_azul)
    print(borde_amarillo)
    
    # Comparar bordes
    print(f'Son iguales? {borde_rojo.esIgualQue(borde_azul)}')
    print(f'Son iguales? {borde_rojo.esIgualQue(borde_amarillo)}')
    
    # Copiar valores
    borde_rojo_copia = borde_rojo.clonar()
    borde_rojo_copia.copiarValores(borde_amarillo)
    
    # Mostrar bordes copiados
    print(borde_rojo_copia)
    print(f'Son iguales? {borde_rojo_copia.esIgualQue(borde_amarillo)}')
    
    # Mostrar propiedades
    print(f'Grosor: {borde_rojo_copia.obtenerGrosor()}')
    print(f'Color: {borde_rojo_copia.obtenerColor()}')

# Ejecutar tester

test_borde()