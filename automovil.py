class Automovil:
    #atributos de instancia
    def _init_(self,marca:str,modelo:str,anio:int,velocidadMaxima:float,velocidadActual:float):
        self.__marca=marca
        self.__modelo=modelo
        self.__anio=anio
        self.__velocidadMaxima=velocidadMaxima
        self.__velocidadActual=velocidadActual
    

    #comandos
    def establecerMarca(self,marca:str):
        self.__marca=marca
    
    def establecerModelo(self,modelo:str):
        self.__modelo=modelo
    
    def establecerAnio(self,anio:int):
        self.__anio=anio

    def establecerVelocidadMaxima(self,velocidadMaxima:float):
        if velocidadMaxima>0:
            self.__velocidadMaxima=velocidadMaxima
    
    def establecerVelocidadActual(self,velocidadActual:float):
        if velocidadActual<self.__velocidadMaxima:
            self.__velocidadActual=velocidadActual
        
    
    def acelerar(self,incrementoVelocidad:int):
        if incrementoVelocidad>0:
            if (self._velocidadActual+incrementoVelocidad < self._velocidadMaxima):
                self.__velocidadActual+=incrementoVelocidad
    
    def desacelerar(self,decrementoVelocidad:int):
        if decrementoVelocidad>0:
            if (self.__velocidadActual-decrementoVelocidad>0):
                self.__velocidadActual-=decrementoVelocidad
    
    def frenarPorCompleto(self):
        self.__velocidadActual=0
    
    #consultas

    def obtenerMarca(self):
        return self.__marca
    
    def obtenerModelo(self):
        return self.__modelo
    
    def obtenerAnio(self):
        return self.__anio
    
    def obtenerVelocidadMaxima(self):
        return self.__velocidadMaxima
    
    def obtenerVelocidadActual(self):
        return self.__velocidadActual
    
    def calcularMinutosParaLlegar(self, distanciaKM: float) -> int:
    
        if self.obtenerVelocidadActual() == 0:
            print("El auto está detenido")
            return None
    
        horas = distanciaKM / self.obtenerVelocidadActual()
        minutos = int (horas * 60)
    
        return minutos

import random

class Tester():
    def test():
        autito=Automovil("renault","clio",2008,160,50)
        cantidad = int(input("Ingresa la cantidad de iteraciones a realizar: "))
        contador=0
        while (contador<cantidad):

            numero_aleatorio =random.randint(0,3)

            if numero_aleatorio==0:
                print("Se genero el numero 0, por lo tanto se va a acelerar 20 km, la velocidad actual es: ",autito.obtenerVelocidadActual())
                autito.acelerar(20)
                print("Ahora la velocidad es: ",autito.obtenerVelocidadActual())
            elif numero_aleatorio==1:
                print("Se genero el numero 1, por lo tanto se va a desacelerar 15 km, la velocidad actual es: ",autito.obtenerVelocidadActual())
                autito.desacelerar(15)
                print("Ahora la velocidad es: ",autito.obtenerVelocidadActual())
            elif numero_aleatorio==2:
                print("Se genero el numero 2, por lo tanto se va a frenar por completo, la velocidad actual es: ",autito.obtenerVelocidadActual())
                autito.frenarPorCompleto()
                print("Ahora la velocidad es: ",autito.obtenerVelocidadActual())
            else:
                print("Se genero el numero 3, por lo tanto se va a calcular minutos para llegar en 50 km, la velocidad actual es: ",autito.obtenerVelocidadActual())
                minutos=autito.calcularMinutosParaLlegar(50)
                print("Los minutos son: ",minutos)
            contador+=1
        
        
    

Tester.test()