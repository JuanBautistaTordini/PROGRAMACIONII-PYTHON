#  empleado.py

'''
1. Empleado (Clase Abstracta y padre)
    Atributos:
        __dni: str
        __nombre: str
        __apellido: str
        __fecha_ingreso: date
    Métodos:
        __init__(dni, nombre, apellido, fecha_ingreso)
        calcular_salario(): float
        __str__(): str
'''

from datetime import date

from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, dni: str, nombre: str, apellido: str, fecha_ingreso: date):
        if not dni or not nombre or not apellido:
            raise ValueError("DNI, nombre y apellido no pueden estar vacíos.")
        if not isinstance(fecha_ingreso, date):
            raise ValueError("La fecha de ingreso debe ser un objeto de tipo date.")
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_ingreso = fecha_ingreso

    def get_dni(self) -> str:
        return self.__dni

    def set_dni(self, dni: str) -> None:
        if not dni:
            raise ValueError("El DNI no puede estar vacío.")
        self.__dni = dni

    def get_nombre(self) -> str:
        return self.__nombre

    def set_nombre(self, nombre: str) -> None:
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre

    def get_apellido(self) -> str:
        return self.__apellido

    def set_apellido(self, apellido: str) -> None:
        if not apellido:
            raise ValueError("El apellido no puede estar vacío.")
        self.__apellido = apellido

    def get_fecha_ingreso(self) -> date:
        return self.__fecha_ingreso

    def set_fecha_ingreso(self, fecha_ingreso: date) -> None:
        if not isinstance(fecha_ingreso, date):
            raise ValueError("La fecha de ingreso debe ser un objeto de tipo date.")
        self.__fecha_ingreso = fecha_ingreso

    @abstractmethod
    def calcular_salario(self) -> float:
        pass
    
    def __str__(self) -> str:
        return f"Empleado: {self.__nombre} {self.__apellido}, DNI: {self.__dni}, Fecha de ingreso: {self.__fecha_ingreso}"
    
    
