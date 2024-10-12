# class Fecha:
#     def __init__(self, dia: int, mes: int, anio: int):
#         # Constructor que inicializa día, mes y año
#         self.dia = dia
#         self.mes = mes
#         self.anio = anio

#     # Comandos para establecer valores
#     def establecerDia(self, dia: int):
#         self.dia = dia

#     def establecerMes(self, mes: int):
#         self.mes = mes

#     def establecerAnio(self, anio: int):
#         self.anio = anio

#     # Consultas para obtener los valores
#     def obtenerDia(self) -> int:
#         return self.dia

#     def obtenerMes(self) -> int:
#         return self.mes

#     def obtenerAnio(self) -> int:
#         return self.anio

#     # Consulta que verifica si la fecha actual es anterior a otra fecha
#     def esAnterior(self, otraFecha: 'Fecha') -> bool:
#         if self.anio < otraFecha.anio:
#             return True
#         elif self.anio == otraFecha.anio:
#             if self.mes < otraFecha.mes:
#                 return True
#             elif self.mes == otraFecha.mes:
#                 return self.dia < otraFecha.dia
#         return False

#     # Método que suma días a la fecha actual
#     def sumaDias(self, cantDias: int) -> 'Fecha':
#         dia = self.dia + cantDias
#         mes = self.mes
#         anio = self.anio

#         while dia > 30:  # Si el día supera los 30 días, avanza al siguiente mes
#             dia -= 30
#             mes += 1
#             if mes > 12:  # Si el mes supera los 12 meses, avanza al siguiente año
#                 mes = 1
#                 anio += 1
#         return Fecha(dia, mes, anio)

#     # Método que retorna una nueva fecha con el día siguiente
#     def diaSiguiente(self) -> 'Fecha':
#         return self.sumaDias(1)

#     # Método que verifica si la fecha es igual a otra fecha
#     def esIgualQue(self, otraFecha: 'Fecha') -> bool:
#         return self.dia == otraFecha.dia and self.mes == otraFecha.mes and self.anio == otraFecha.anio

# # Clase tester
# if __name__ == "__main__":
#     # Crear dos fechas
#     fecha1 = Fecha(28, 12, 2023)
#     fecha2 = Fecha(1, 1, 2024)

#     # Pruebas de comparación
#     print(f"Fecha 1 es anterior a Fecha 2: {fecha1.esAnterior(fecha2)}")  # True

#     # Prueba de suma de días
#     nueva_fecha = fecha1.sumaDias(5)
#     print(f"Sumar 5 días a {fecha1.obtenerDia()}/{fecha1.obtenerMes()}/{fecha1.obtenerAnio()} -> {nueva_fecha.obtenerDia()}/{nueva_fecha.obtenerMes()}/{nueva_fecha.obtenerAnio()}")

#     # Prueba de día siguiente
#     siguiente_dia = fecha1.diaSiguiente()
#     print(f"El día siguiente de {fecha1.obtenerDia()}/{fecha1.obtenerMes()}/{fecha1.obtenerAnio()} es {siguiente_dia.obtenerDia()}/{siguiente_dia.obtenerMes()}/{siguiente_dia.obtenerAnio()}")

#     # Prueba de igualdad
#     print(f"Fecha 1 es igual a Fecha 2: {fecha1.esIgualQue(fecha2)}")  # False

'''
a) Rojo (R): Intensidad de la luz roja (de 0 a 255). 
b) Verde (G): Intensidad de la luz verde (de 0 a 255). 
c) Azul (B): Intensidad de la luz azul (de 0 a 255). 

d) Blanco se forma con R=255, G=255, B=255. 
e) Negro se forma con R=0, G=0, B=0. 
f) Gris tiene valores iguales para R, G, y B (por ejemplo, R=50, G=50, B=50)
'''

# class Color:
#     def __init__ (self, rojo=255, verde=255, azul=255):
#         self._rojo = self._validar_color(rojo)
#         self._verde = self._validar_color(verde)
#         self._azul = self._validar_color(azul)

#     def _validar_color(self, valor):
#         # Método auxiliar para validar que el color esté entre 0 y 255
#         return max(0, min(valor, 255))

#     #comandos

#     def variar(self, valor):
#         #suma el valor
#         self.variarRojo(valor)
#         self.variarVerde(valor)
#         self.variarAzul(valor)
    
#     # modifica la componente de rojo sumándole un valor 
#     # dado. Ídem para azul (variarAzul(val:entero)) y verde 
#     # (variarVerde(val:entero)).

#     def variarRojo(self, valor):
#         self._rojo = self._validar_color(self._rojo + valor)
    
#     def variarVerde(self, valor):
#         self._verde = self._validar_color(self._verde + valor)
    
#     def variarAzul(self, valor):
#         self._azul = self._validar_color(self._azul + valor)
    
#     def establecerRojo(self, valor):
#         self._rojo = self._validar_color(valor)
    
#     def establecerVerde(self, valor):
#         self._verde = self._validar_color(valor)
    
#     def establecerAzul(self, valor):
#         self._azul = self._validar_color(valor)
    
#     def copiar(self, otroColor):
#         self._rojo = otroCOlor._rojo
#         self._verde = otroColor._verde
#         self._azul = otroColor._azul
    
#     #Consultas
    
#     def obtenerRojo(self):
#         return self._rojo
    
#     def obtenerVerde(self):
#         return self._verde
    
#     def obtenerAzul(self):
#         return self._azul
    
#     #Retorna verdader so el objeto que recibe el mensaje representa el color rojo
#     def esRojo(self):
#         return self._rojo == 255 and self._verde == 0 and self._azul == 0
    
#     #idem anterior, Gris tiene valores iguales para R, G, y B (por ejemplo, R=50, G=50, B=50
#     def esGris(self):
#         return self._rojo ==  self._verde == self._azul
    
#     #Negro se forma con R=0, G=0, B=0
#     def esNegro(self):
#         return self._rojo == 0 and self._verde == 0 and self._azul == 0
    
#     def complemento(self):
#         #retorna complementario
#         return Color(255 - self._rojo, 255 - self._verde, 255 - self._azul)
    
#     def esIgualQue(self, otroColor):
#         # retorna verdadero si ambos objetos son equivalentes
#         return (self._rojo == otroColor._rojo and
#                 self._verde == otroColor._verde and
#                 self._azul == otroColor._azul)
    
#     def clonar(self):
#         #Clonar el color actual
#         return Color(self._rojo, self._verde, self._azul)

# # Clase tester

# if __name__ == "__main__":
#     # Crear colores
#     color1 = Color()

#     print(f"color inicial: R={color1.obtenerRojo()} G={color1.obtenerVerde()} B={color1.obtenerAzul()}")

#     #personalizado
#     colorPer = Color(100, 90, 100)
#     print(f"color personalizado: R={colorPer.obtenerRojo()} G={colorPer.obtenerVerde()} B={colorPer.obtenerAzul()}")

#     #variar
#     colorPer.variarRojo(20)
#     colorPer.variarVerde(15)
#     colorPer.variarAzul(10)
#     print(f"color despues de variar: R={colorPer.obtenerRojo()} G={colorPer.obtenerVerde()} B={colorPer.obtenerAzul()}")

#     #Verificacion

#     #Es rojo?
#     print(f"Es rojo? {colorPer.esRojo()}")
#     #Es gris?
#     print(f"Es gris? {colorPer.esGris()}")
#     #Es negro?
#     print(f"Es negro? {colorPer.esNegro()}")

#     #obtener complementario
#     complemento = colorPer.complemento()
#     print(f"complementario: R={complemento.obtenerRojo()} G={complemento.obtenerVerde()} B={complemento.obtenerAzul()}")

#     #igualdad
#     colorPer2 = Color(100, 90, 100)
#     print(f"Son iguales? {colorPer.esIgualQue(colorPer2)}")

#     #clonar
#     colorClonado = colorPer.clonar()
#     print(f"Color clonado: R={colorClonado.obtenerRojo()} G={colorClonado.obtenerVerde()} B={colorClonado.obtenerAzul()}")

#     #clonado es igual a colorPer?
#     print(f"Clonado es igual a colorPer? {colorClonado.esIgualQue(colorPer)}")


class Especie:
    def __init__(self, nombre: str):
        self._nombre = nombre
        #cantidad de hembras
        self._hembras = 0
        # cantidad de machos
        self._machos = 0
        #ritmo de crecimiento anual de la población
        self._ritmo = 0.0
    
    #Comandos
    
    #### Establecer ####
    def establecerHembras(self, cantHembras: int):
        #valor no negativo
        if cantHembras >= 0:
            self._hembras = cantHembras
        else:
            print("Cantidad de hembras no válida.")
    
    def establecerMachos(self, cantMachos: int):
        #valor no negativo
        if cantMachos >= 0:
            self._machos = cantMachos
        else:
            print("Cantidad de machos no válida.")
    
    def establecerRitmo(self, ritmo: float):
        self._ritmo = ritmo
    
    #### Actualizar ####

    def actualizarHembras(self, cantHembras: int):
        #nunca puede ser menor a cero
        self._hembras = max(0, self._hembras + cantHembras)
    
    def actualizarMachos(self):
        #nunca puede ser menor a cero
        self._machos = max(0, self._machos + cantMachos)
    
    def actualizarRitmo(self):
        self._ritmo = ritmo
    
    #### Consultar ####

    def poblacionActual(self):
        #cantidad total de hembras y machos
        return self._hembras + self._machos

    def poblacionEstimada(self, anios: int) -> int:
        return int(self.poblacionActual() * (1 + self._ritmo) ** anios)

    def aniosParaPoblacion(self, poblacion) -> int:
        actual = self.poblacionActual()
        if actual <= 0 or self._ritmo <= 0:
            return -1  # No alcanzará la población
        anios = 0
        while actual < poblacion:
            actual *= (1 + self._ritmo)
            anios += 1
        return anios

    def riesgo(self) -> str:
        #(“verde” si el ritmo de crecimiento es positivo, “amarillo” si es nulo y “rojo” si es negativo)
        #verde
        if self._ritmo > 0:
            return "VERDE"
        elif self._ritmo == 0:
            return "AMARILLO"
        else: 
            return "ROJO"

    def masHembras(self) -> bool:
        return self._hembras > self._machos

    def mayorRitmo(self, otraEspecie) -> 'Otra Especie':
        return self._ritmo > otraEspecie._ritmo

    def clonar(self) -> 'Especie':
        clon = Especie(self.__nombre)
        clon.establecerHembras(self._hembras)
        clon.establecerMachos(self._machos)
        clon.establecerRitmo(self._ritmo)
        return clon

    def toString(self) -> str:
        return f"Especie: {self._nombre}, Machos: {self._machos}, Hembras: {self._hembras}, Ritmo: {self._ritmo}"
    
'''clase tester que verifique los servicios provistos por Especie con 
valores ingresados por el usuario para nombre y ritmo y generados al azar 
para machos y hembras dentro de un rango establecido'''

#Clase Tester
import random

class Tester:
    def __init__(self):

        ### ESTABLECER NOMBRE Y RITMO ###

        #pedir nombre:
        nombre = input("Nombre de la especie: ")
        #pedir ritmo:
        ritmo = float(input("Ritmo: "))

        especie1 = Especie(nombre)
        especie1.establecerRitmo(ritmo)


        ### ESTABLECER HEMBRA MACHO ###

        #generar hembras y machos al azar dentro del rango
        hembras = random.randint(0, 100)
        machos = random.randint(0, 100)

        especie1.establecerMachos(machos)
        especie1.establecerHembras(hembras)
        
        print(especie1.toString())
        print(f"Población actual: {especie1.poblacionActual()}")
        print(f"Nivel de riesgo: {especie1.riesgo()}")
        print(f"Más hembras que machos: {'Sí' if especie1.masHembras() else 'No'}")

        anios = int(input("Ingrese cantidad de años para estimar población: "))
        print(f"Población estimada en {anios} años: {especie1.poblacionEstimada(anios)}")

        poblacion_objetivo = int(input("Ingrese una población objetivo: "))
        anios_necesarios = especie1.aniosParaPoblacion(poblacion_objetivo)
        if anios_necesarios == -1:
            print("La especie no alcanzará esa población con el ritmo actual.")
        else:
            print(f"Años necesarios para alcanzar la población de {poblacion_objetivo}: {anios_necesarios}")

if __name__ == "__main__":
    tester = Tester()
