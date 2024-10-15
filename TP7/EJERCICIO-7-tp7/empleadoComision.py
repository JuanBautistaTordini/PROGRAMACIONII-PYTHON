# empleadoComision.py

'''
EmpleadoComision (Hereda de Empleado)
    Atributos:
        __salario_minimo: float
        __clientes_captados: int
        __monto_por_cliente: float
    Métodos:
        __init__(dni, nombre, apellido, fecha_ingreso, salario_minimo, clientes_captados, monto_por_cliente)
        calcular_salario(): float
'''

from empleado import Empleado

from datetime import date

class EmpleadoComision(Empleado):
    def __init__(self, dni: str, nombre: str, apellido: str, fecha_ingreso: date, salario_minimo: float, clientes_captados: int, monto_por_cliente: float):
        super().__init__(dni, nombre, apellido, fecha_ingreso)
        if salario_minimo <= 0:
            raise ValueError("El salario mínimo debe ser mayor que cero.")
        if clientes_captados < 0:
            raise ValueError("El número de clientes captados no puede ser negativo.")
        if monto_por_cliente <= 0:
            raise ValueError("El monto por cliente debe ser mayor que cero.")
        self.__salario_minimo = salario_minimo
        self.__clientes_captados = clientes_captados
        self.__monto_por_cliente = monto_por_cliente

    def get_salario_minimo(self) -> float:
        return self.__salario_minimo

    def set_salario_minimo(self, salario_minimo: float) -> None:
        if salario_minimo <= 0:
            raise ValueError("El salario mínimo debe ser mayor que cero.")
        self.__salario_minimo = salario_minimo

    def get_clientes_captados(self) -> int:
        return self.__clientes_captados

    def set_clientes_captados(self, clientes_captados: int) -> None:
        if clientes_captados < 0:
            raise ValueError("El número de clientes captados no puede ser negativo.")
        self.__clientes_captados = clientes_captados

    def get_monto_por_cliente(self) -> float:
        return self.__monto_por_cliente

    def set_monto_por_cliente(self, monto_por_cliente: float) -> None:
        if monto_por_cliente <= 0:
            raise ValueError("El monto por cliente debe ser mayor que cero.")
        self.__monto_por_cliente = monto_por_cliente
        
    def calcular_salario(self) -> float:
        return self.__salario_minimo + (self.__clientes_captados * self.__monto_por_cliente)
    
    def __str__(self) -> str:
        return f"Empleado Comisión: {self.get_nombre()} {self.get_apellido()}, DNI: {self.get_dni()}, Fecha de ingreso: {self.get_fecha_ingreso()}, Salario mínimo: {self.__salario_minimo}, Clientes captados: {self.__clientes_captados}, Monto por cliente: {self.__monto_por_cliente}"
