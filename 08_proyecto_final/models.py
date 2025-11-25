from datetime import datetime, timedelta

class Transaccion:
    def __init__(self, monto, descripcion,categoria,tipo):
        self.monto = monto
        self.descripcion = descripcion
        self.categoria = categoria 
        self.tipo = tipo 
        self.fecha = datetime.now()

    def __str__(self):
        return f"[{self.fecha.year}-{self.fecha.month}-{self.fecha.day}] {self.tipo}: ${self.monto} - {self.descripcion}"


class Cuenta:
    def __init__(self):
        self.transacciones = []

    def agregar_transaccion(self,transaccion):
        self.transacciones.append(transaccion)

    def calcular_balance(self):
        balance = 0
        for t in self.transacciones:
            if t.tipo=="Gasto":
                balance -= t.monto
            else:
                balance += t.monto
        return balance