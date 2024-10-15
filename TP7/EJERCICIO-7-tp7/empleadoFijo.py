# empleadoFijo.py

'''
EmpleadoFijo (Hereda de Empleado)
    Atributos:
        __sueldo_basico: float
        __anios_empresa: int
    Métodos:
        __init__(dni, nombre, apellido, fecha_ingreso, sueldo_basico, anios_empresa)
        calcular_salario(): float
'''

from empleado import Empleado

from datetime import date

class EmpleadoFijo(Empleado):
    def __init__(self, dni: str, nombre: str, apellido: str, fecha_ingreso: date, sueldo_basico: float, anios_empresa: int):
        super().__init__(dni, nombre, apellido, fecha_ingreso)
        if sueldo_basico <= 0:
            raise ValueError("El sueldo básico debe ser mayor que cero.")
        if anios_empresa < 0:
            raise ValueError("Los años en la empresa no pueden ser negativos.")
        self.__sueldo_basico = sueldo_basico
        self.__anios_empresa = anios_empresa

    def get_sueldo_basico(self) -> float:
        return self.__sueldo_basico

    def set_sueldo_basico(self, sueldo_basico: float) -> None:
        if sueldo_basico <= 0:
            raise ValueError("El sueldo básico debe ser mayor que cero.")
        self.__sueldo_basico = sueldo_basico

    def get_anios_empresa(self) -> int:
        return self.__anios_empresa

    def set_anios_empresa(self, anios_empresa: int) -> None:
        if anios_empresa < 0:
            raise ValueError("Los años en la empresa no pueden ser negativos.")
        self.__anios_empresa = anios_empresa

    def calcular_salario(self) -> float:
        return self.__sueldo_basico + (self.__anios_empresa * 1000)
    
    def __str__(self) -> str:
        return f"Empleado Fijo: {self.get_nombre()} {self.get_apellido()}, DNI: {self.get_dni()}, Fecha de ingreso: {self.get_fecha_ingreso()}, Sueldo básico: {self.__sueldo_basico}, Años en la empresa: {self.__anios_empresa}"