'''
1. Analice si las siguientes definiciones son correctas

a. Desde el punto de vista del diseño de un sistema orientado a objetos, una
clase es un “molde” que establece solamente los atributos de una entidad.

RESPUESTA= Una clase define tanto los atributos como los comportamientos que puede tener un objeto.


b. En la Programación Orientada a Objetos se busca tratar a toda entidad como
si fuera un objeto en la vida real, donde cada objeto tiene algunas
propiedades y comportamientos.

RESPUESTA= Es la definicion exacta de POO 

c. El diagrama de una clase sólo especifica los atributos del objeto.

RESPUESTA= Un diagrama no solo especifica los atributos del objeto sino que tambien los comportaminetos

d. Los objetos tienen atributos (características) y métodos (funciones)
asociados.

RESPUESTA= Si, los atributos son las caraccteristicas que distinguen a los objetos, mientras que los metodos son aquellos que definen las acciones de un objeto

e. Un constructor es un método que se invoca cuando se crea un objeto.

RESPUESTA= Un constructor es un metodo especial que se invoca automaticamente al crear una clase, por lo tanto, se invoca cuando se crea un objeto.

f. Un comando es un método que nunca modifica los valores del objeto.

RESPUESTA= Un comando es un metodo que modifica los valores del objeto, pero nunca se invoca automaticamente al crear un objeto.

g. Una consulta es un método que modifica los valores del objeto.

RESPUESTA= Un consulta es un metodo que no modifica el estado del objeto, sino que se le consulta y se brinda informacion sobre dicho objeto

'''

#2a
# a. implementar en python la clase Empleado.

# class Empleado:
#     # Constructor con parámetros
#     def __init__(self, legajo: int, cantHoras: int = 0, valorHora: float = 0.0):
#         self.legajo = legajo
#         self.horasTrabajadasMes = cantHoras
#         self.valorHora = valorHora
    
#     # Comandos:
#     def horas_trabajadas(self, cantHoras: int):
#         self.horasTrabajadasMes = cantHoras
    
#     def establecer_valor_hora(self, valorHora: float):
#         self.valorHora = valorHora
    
#     # Consultas:
#     def obtener_legajo(self) -> int:
#         return self.legajo
    
#     def obtener_horas_trabajadas(self) -> int:
#         return self.horasTrabajadasMes
    
#     def obtener_valor_hora(self) -> float:
#         return self.valorHora
    
#     def obtener_sueldo(self) -> float:
#         return self.horasTrabajadasMes * self.valorHora

# # Testear el constructor con todos los parámetros

# def tester():
#     # Solicitar los datos del empleado
#     legajo = int(input("Legajo del empleado: "))
    
#     # Crear el objeto empleado con el legajo, inicialmente sin horas ni valor por hora
#     empleado = Empleado(legajo)
    
#     # Modificar las horas trabajadas y el valor de la hora usando los métodos de la clase
#     horas_trabajadas = int(input("Cantidad de horas trabajadas: "))
#     empleado.horas_trabajadas(horas_trabajadas)
    
#     valor_hora = float(input("Valor por hora: "))
#     empleado.establecer_valor_hora(valor_hora)
    
#     # Mostrar los resultados
#     print(f"\nLegajo del empleado: {empleado.obtener_legajo()}")
#     print(f"Sueldo del empleado: {empleado.obtener_sueldo():.2f}")

# tester()

# class Vinoteca:
#     capacidadMaxima = 5000  # Capacidad máxima de cada sección

#     # Constructor
#     def __init__(self):
#         # Atributos de instancia
#         self.cantJugos = Vinoteca.capacidadMaxima
#         self.cantBlancos = Vinoteca.capacidadMaxima
#         self.cantTintosJovenes = Vinoteca.capacidadMaxima
#         self.cantTintosAnejados = Vinoteca.capacidadMaxima

#     # Comandos para reponer productos
#     def reponerJugos(self):
#         self.cantJugos = Vinoteca.capacidadMaxima

#     def reponerVinosBlancos(self):
#         self.cantBlancos = Vinoteca.capacidadMaxima

#     def reponerVinosTintoJoven(self):
#         self.cantTintosJovenes = Vinoteca.capacidadMaxima

#     def reponerVinosTintoAnejado(self):
#         self.cantTintosAnejados = Vinoteca.capacidadMaxima

#     # Comandos para vender productos
#     def venderJugos(self, unidades: int):
#         if unidades > self.cantJugos:
#             self.cantJugos = 0
#             print(f"No se pudo completar la venta de jugos. Se vendieron {unidades_vendidas} unidades.")
#         else:
#             self.cantJugos -= unidades

#     def venderVinosBlancos(self, unidades: int):
#         if unidades > self.cantBlancos:
#             self.cantBlancos = 0
#             print(f"No se pudo completar la venta de vinos blancos. Se vendieron {unidades_vendidas} unidades.")
#         else:
#             self.cantBlancos -= unidades

#     def venderVinosTintosJovenes(self, unidades: int):
#         if unidades > self.cantTintosJovenes:
#             self.cantTintosJovenes = 0
#             print(f"No se pudo completar la venta de vinos tintos jóvenes. Se vendieron {unidades_vendidas} unidades.")
#         else:
#             self.cantTintosJovenes -= unidades

#     def venderVinosTintosAnejados(self, unidades: int):
#         if unidades > self.cantTintosAnejados:
#             self.cantTintosAnejados = 0
#             print(f"No se pudo completar la venta de vinos tintos añejados. Se vendieron {unidades_vendidas} unidades.")
#         else:
#             self.cantTintosAnejados -= unidades

#     # Consultas para obtener las cantidades actuales de los productos
#     def obtenerCantidadJugos(self) -> int:
#         return self.cantJugos

#     def obtenerCantidadVinosBlancos(self) -> int:
#         return self.cantBlancos

#     def obtenerCantidadVinosTintosJovenes(self) -> int:
#         return self.cantTintosJovenes

#     def obtenerCantidadVinosTintosAnejados(self) -> int:
#         return self.cantTintosAnejados


# # Clase tester para verificar los servicios de la clase Vinoteca

# class Tester():
#     def test():
#         # Crear la instancia de la Vinoteca
#         vinoteca = Vinoteca()

#         #Mostrar Cantidad
#         print(f"Cantidad de jugos: {vinoteca.obtenerCantidadJugos()}")
#         print(f"Cantidad de vinos blancos: {vinoteca.obtenerCantidadVinosBlancos()}")
#         print(f"Cantidad de vinos tintos jóvenes: {vinoteca.obtenerCantidadVinosTintosJovenes()}")
#         print(f"Cantidad de vinos tintos añejados: {vinoteca.obtenerCantidadVinosTintosAnejados()}")
        
#         # Vender unidades
#         venta = int(input("Cantidad Vender Juegos: "))
#         vinoteca.venderJugos(venta)

#         print(f"Cantidad de jugos: {vinoteca.obtenerCantidadJugos()}")

#         #Se continua..

# # Ejecutar el tester
# Tester.test()

"""Se requiere un programa que modele el concepto de un Automóvil. Para simplificar
consideraremos que un automóvil tiene solamente los siguientes atributos:
Marca: el nombre del fabricante.
Modelo: nombre del modelo.
Año: año de fabricación.
Velocidad máxima: velocidad máxima soportada por el vehículo en km/h.
Velocidad actual: velocidad del vehículo en un momento dado en km/h.

Es importante tener en cuenta que no se debe acelerar más allá de la velocidad
máxima permitida para el automóvil. De igual manera, tampoco es posible
desacelerar a una velocidad negativa. Si se cumplen estos casos, se debe
establecer la velocidad en el límite correspondiente y mostrar por pantalla un
mensaje.
El tiempo estimado en horas se calcula como el cociente entre la distancia en 
kilómetros a recorrer y la velocidad actual (en km/h), multiplicando este valor por 60
obtenemos la cantidad de minutos. Considerar el caso especial cuando el auto se
encuentre detenido, en este caso mostrar un mensaje indicando que “el auto está
detenido y no se puede calcular el tiempo para llegar”.
a. implementar la clase en python
b. implementar una clase tester que cree un objeto de clase Automovil, y que
pida al usuario la cantidad de iteraciones a realizar, luego para cada iteración
deberá generar un número aleatorio entre 0 y 3 que determinará la operación
a realizar:
● 0: acelerar(20)
● 1: desacelerar(15)
● 2: frenarPorCompleto()
● 3: calcularMinutosParaLlegar(50)
En cada iteracion se debe mostrar el valor que se modificará, la acción a
realizar y el valor modificado luego de la acción. Por ejemplo, si tocó el valor
0 muestra: “velocidad = 100, acelerar, velocidad actual = 120”. En el caso del
calculo del tiempo para llegar debe mostrar el tiempo para llegar.
c. Realizar otra clase tester con la misma lógica, pero las operaciones a realizar
deben recibir parámetros aleatorios (coherentes)
"""

# class Automovil():
#     #Constructor Y atributos
#     def __init__(self, marca: str, modelo: str, anio:int, velocidadMaxima: float, VelocidadMinima: float):
#         self.__marca = marca
#         self.__modelo = modelo
#         self.__anio = anio
#         self.__velocidadMaxima = velocidadMaxima
#         self.__velocidadActual = VelocidadMinima
#     #comandos
#     def establecerMarca(self):
#         self.__marca = marca
#     def establecerModelo(self):
#         self.__modelo = modelo
#     def establecerAnio(self):
#         self.__anio = anio
#     def establecerVelocidadMaxima(self, velocidadMaxima:float):
#         if velocidadMaxima > 0:
#             self.__velocidadActual = VelocidadMinima
#     def establecerVelocidadActual(self, velocidadActual:float):
#         if velocidadActual < self.__velocidadMaxima:
#             self.__velocidadActual = velocidadActual
#     def acelerar(self, incrementoVelocidad: int):
#         if incrementoVelocidad > 0:
#             if(self, __velocidadActual + incrementoVelocidad< self,__velocidadMaxima):
#                 self.__velocidadActual += incrementoVelocidad
#     def desacelerar(self, decrementoVelocidad: int):
#         if decrementoVelocidad > 0:
#             if(self, __velocidadActual - decrementoVelocidad> VelocidadMinima):
#                 self.__velocidadActual -= decrementoVelocidad
#     def frenarPorCompleto(self):
#         self.__velocidadActual = 0
#     #consultas
#     def obtenerMarca(self):
#         return self.__marca
#     def obtenerModelo(self):
#         return self.__modelo
#     def obtenerAnio(self):
#         return self.__anio
#     def obtenerVelocidadMaxima(self):
#         return self.__velocidadMaxima
#     def obtenerVelocidadActual(self):
#         return self.__velocidadActual
#     def calcularMinutosParaLlegar(self, distanciaKM: float) -> int:
#         """cociente entre la distancia en kilómetros a recorrer y la velocidad actual (en km/h)"""
#         if self.__velocidadActual == 0:
#             print("El auto está detenido y no se puede calcular el tiempo para llegar.")
#             return None
#         else:
#             """multiplicando este valor por 60 obtenemos la cantidad de minutos."""
#             return int(distanciaKM * 60 / self.__velocidadActual)
# import random
# class Tester():
#     def test():
#         auto = Automovil("renault", "clio", 2008, 180, 20)
#         iteracion = int(input("0 para acelerar 20 - 1 para desacelerar 15 - 2 para frenar - 3 para calcular minutos"))
#         contador = 0

#         while (contador < iteracion):

#             numero_aleatorio = random.randint(0,3)

#             if numero_aleatorio==0:
#                 print("Se genero el numero 0, por lo tanto se va a acelerar 20 km, la velocidad actual es: ",auto.obtenerVelocidadActual())
#                 auto.acelerar(20)
#                 print("Ahora la velocidad es: ",auto.obtenerVelocidadActual())
#             elif numero_aleatorio==1:
#                 print("Se genero el numero 1, por lo tanto se va a desacelerar 15 km, la velocidad actual es: ",auto.obtenerVelocidadActual())
#                 auto.desacelerar(15)
#                 print("Ahora la velocidad es: ",auto.obtenerVelocidadActual())
#             elif numero_aleatorio==2:
#                 print("Se genero el numero 2, por lo tanto se va a frenar por completo, la velocidad actual es: ",auto.obtenerVelocidadActual())
#                 auto.frenarPorCompleto()
#                 print("Ahora la velocidad es: ",auto.obtenerVelocidadActual())
#             else:
#                 print("Se genero el numero 3, por lo tanto se va a calcular minutos para llegar en 50 km, la velocidad actual es: ",auto.obtenerVelocidadActual())
#                 minutos=auto.calcularMinutosParaLlegar(50)
#                 print("Los minutos son: ",minutos)
#             contador+=1
# #tester
# Tester.test()

'''Condiciones: 
-su nivel de energía, el cual nunca 
puede disminuir por debajo de 0 ni superar el máximo de 
100

-Mientras duerme no puede hacer ninguna otra acción, 
a menos que antes se lo despierte

-Ninguna mascota puede 
realizar más de tres acciones de desgaste de energía en 
forma consecutiva

 estados que debes gestionar: Energía, Diversión e Higiene
 Cada estado se representa con un valor numérico que puede variar entre 0 (muy 
bajo) y 100 (muy alto)

a. Comer: aumenta el nivel de energía en 20 puntos. 
b. Beber: aumenta el nivel de energía en 10 puntos. 
c. Jugar: aumenta la diversión en 40 puntos, pero reduce la energía en 20 
puntos y la higiene en 15 puntos. 
d. Caminar: aumenta la diversión en 20 puntos, reduce energía en 10 puntos y 
la higiene en 8 puntos. 
e. Saltar: aumenta la diversión en 10 puntos, reduce energía en 15 puntos y la 
higiene en 10 puntos. 
f. Dormir: aumenta la energía en 20 puntos, pero reduce la diversión en 10 
puntos. 
g. Bañar: aumenta la higiene en 40 puntos, pero reduce la diversión en 10 
puntos.
Si el nivel de energía de la mascota llega a 0, lamentablemente dejará de existir y no 
podrá realizar ninguna actividad más

● Humor Feliz: Si energía, diversión e higiene están todos por encima de 70. 
● Humor Alegre: Si al menos dos de los tres (energía, diversión, higiene) están 
entre 50 y 70. 
● Humor Neutral: Si al menos dos de los tres están entre 30 y 50. 
● Humor Triste: Si al menos dos de los tres están entre 10 y 30. 
● Humor Muy Triste: Si al menos dos de los tres están por debajo de 10.


Implementar la clase MascotaVirtual modelada por el siguiente diagrama, pueden 
agregarle los métodos que consideren necesarios.

'''

# class MascotaVirtual:
#     #Atributos de la clase MascotaVirtual
#     MAX_VALOR = 100
#     MIN_VALOR = 0

#     #Atributos de instancia
#     def __init__(self, nombre: str):
#         self.nombre = nombre
#         self.energia = self.MAX_VALOR
#         self.diversion = self.MAX_VALOR
#         self.higiene = self.MAX_VALOR
#         self.dormido = False
#         cantActividadesDesgaste = 0
    
#     #Comer: aumenta el nivel de energía en 20 puntos. 
#     def comer(self):
#         if self._PuedeRealizar():
#             self._modificarEnergia(20)
#             self._resetearDesgaste()
    
#     #Beber: aumenta el nivel de energía en 10 puntos. 
#     def beber(self):
#         if self._PuedeRealizar():
#             self._modificarEnergia(10)
#             self._resetearDesgaste()

#     #Dormir: aumenta la energía en 20 puntos, pero reduce la diversión en 10 puntos. 
#     def dormir(self):
#         if not self.dormido:
#             self.dormido = True
#             self._modificarEnergia(20)
#             self._modificarDiversion(10)
    
#     def despertar(self):
#         if self.dormido:
#             self.dormido = False
        
#     #Jugar: aumenta la diversión en 40 puntos, pero reduce la energía en 20 puntos y la higiene en 15 puntos. 
#     def jugar(self):
#         if self._PuedeRealizar():
#             self._modificarDiversion(40)
#             self._modificarEnergia(-20)
#             self._modificarHigiene(15)
    
#     #Caminar: aumenta la diversión en 20 puntos, reduce energía en 10 puntos y la higiene en 8 puntos.
#     def caminar(self):
#         if self._PuedeRealizar():
#             self._modifiacarDiversion(20)
#             self._modificarEnergia(-10)
#             self._modificarHigiene(-8)
#     #Saltar: aumenta la diversión en 10 puntos, reduce energía en 15 puntos y la higiene en 10 puntos. 
#     def saltar(self):
#         if self._PuedeRealizar():
#             self._modificarDiversion(10)
#             self._modificarEnergia(-15)
#             self._modificarHigiene(10)
#     #Bañar: aumenta la higiene en 40 puntos, pero reduce la diversión en 10 puntos.
#     def baniar(self):
#         if self._PuedeRealizar():
#             self._modificarHigiene(40)
#             self._modificarDiversion(-10)

#     #Consultas
#     def obtenerNombre(self):
#         return self.nombre

#     def obtenerEnergia(self):
#         return self.energia

#     def obtenerDiversion(self):
#         return self.diversion

#     def obtenerHigiene(self):
#         return self.higiene

#     def estaDormido(self): 
#         return self.dormido

#     def obtenerHumor(self):
#         return self._Humor

#     def estaVivo(self):
#         return self.energia > self.MIN_VALOR

#     def _modificarEnergia(self, valor):
#         self.energia = max(self.MIN_VALOR, min(self.energia + valor, self.MAX_VALOR))
    
#     def _modificarDiversion(self, valor):
#         self.diversion = max(self.MIN_VALOR, min(self.diversion + valor, self.MAX_VALOR))
    
#     def _modificarHigiene(self, valor):
#         self.higiene = max(self.MIN_VALOR, min(self.higiene + valor, self.MAX_VALOR))
    
#     def _PuedeRealizar(self):
#         if self.dormido:
#             print(f"{self.nombre} No puede realizar nada porque está dormido")
#             return false
#         if self.cantActividadesDesgaste >= 3:
#             print(f"{self.nombre} No puede realizar más de tres acciones de desgaste, a dormir.")
#             return false
#         return true
    
#     def definirDesgaste(self):
#         self.cantActividadesDesgaste += 1
    
#     def _resetearDesgaste(self):
#         self.cantActividadesDesgaste = 0

#     def _determinarHumor(self):
#         energia = self.energia
#         diversion = self.diversion
#         higiene = self.higiene

#         if energia > 70 and diversion > 70 and higiene > 70:
#             return "Feliz"
#         elif (energia > 50 and diversion > 50) or (energia > 50 and higiene > 50) or (diversion > 50 and higiene > 50):
#             return "Alegre"
#         elif (energia > 30 and diversion > 30) or (energia > 30 and higiene > 30) or (diversion > 30 and higiene > 30):
#             return "Neutral"
#         elif (energia > 10 and diversion > 10) or (energia > 10 and higiene > 10) or (diversion > 10 and higiene > 10):
#             return "Triste"
#         else:
#             return "Muy Triste"

# class Atleta:
#     #atributos
#     MAX_VALOR = 100
#     MIN_VALOR = 0

#     #Constructor
#     def __init__(self, nombre: str):
#         self.nombre = nombre
#         self.energia = Atleta.MAX_VALOR
#         self.destreza = Atleta.MIN_VALOR
#         self.contador = 0

#     #Comando entrenar : consume energía y aumenta la destreza cada 5 entrenamientos
#     def entrenar(self):
#         #confirmacion si el atleta puede entrenar
#         if self.energia >= 5:
#             self.energia -= 5 #resta 5 puntos de energia
#             self.contador += 1 #contador en uno mas que el anterior

#             print(f"{self.nombre} ha entrenado. Energía restante: {self.energia}")

#             #mejora de destreza
#             if self.contador == 5:
#                 self.destreza += 1
#                 #reseteo de contador
#                 self.contador = 0

#                 print(f"{self.nombre} ha mejorado su destreza a {self.destreza}")
#         else:
#             print(f"{self.nombre} no tiene suficiente energia para entrenar")
    
#     #comando para descansar
#     def descansar(self):
#         #cuando descansa recupera 20
#         self.energia += 20
#         print(f"{self.nombre} ha descansado. Energía restante: {self.energia}")

#     #Los servicios mismaDestrezaQue y esMejorQue comparan a los atletas por su nivel de destreza.
#     def mismaDestrezaQue(self, otroAtleta):
#         return self.destreza == otroAtleta.destreza
    
#     def esMejorQue(self, otroAtleta):
#         return self.destreza > otroAtleta.destreza
    
#     #b) Clase Tester para verificar los servicios de la clase Atleta
#     class Tester:
#         def __init__(self):
#             self.atletas = []
#             self.crearAtletas()
#             self.mostrarAtletas()
#             self.testEntrenar()
#             self.testDescansar()
#             self.testMismaDestrezaQue()
#             self.testEsMejorQue()
        
#         def crearAtletas(self):
#             self.atletas.append(Atleta("Atleta 1"))
#             self.atletas.append(Atleta("Atleta 2"))
#             self.atletas.append(Atleta("Atleta 3"))
        
#         def mostrarAtletas(self):
#             print("Atletas:")
#             for atleta in self.atletas:
#                 print(f"Nombre: {atleta.nombre}, Energia: {atleta.energia}, Destreza: {atleta.destreza}")
#                 print("-------------------------")
        
#         def testEntrenar(self):
#             for atleta in self.atletas:
#                 atleta.entrenar()
#                 print("-------------------------")
        
#         def testDescansar(self):
#             for atleta in self.atletas:
#                 atleta.descansar()
#                 print("-------------------------")
        
#         def testMismaDestrezaQue(self):
#             atleta1 = self.atletas[0]
#             atleta2 = self.atletas[1]
#             print(f"{atleta1.nombre} misma destreza que {atleta2.nombre}: {atleta1.mismaDestrezaQue(atleta2)}")
#             print("-------------------------")
        
#         def testEsMejorQue(self):
#             atleta1 = self.atletas[0]
#             atleta2 = self.atletas[1]
#             print(f"{atleta1.nombre} es mejor que {atleta2.nombre}: {atleta1.esMejorQue(atleta2)}")
#             print("-------------------------")
# # Ejecutar la prueba

# tester = Atleta.Tester()


