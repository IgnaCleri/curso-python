from models import Transaccion, Cuenta
from utils import validar_numero

mi_cuenta = Cuenta()

while True:
    opcion = input("Inserte operacion a realizar:" + "\n" + "1.Agregar Ingreso" + "\n" + "2.Agregar Gasto" + "\n" + "3.Mostrar Balance" + "\n" + "4.Salir" + "\n")
    opcion_valida = validar_numero(opcion)
    if opcion_valida:
        if opcion_valida == 1 :
            monto = input("Ingrese el monto a ingresar:" + "\n")
            monto_validado = validar_numero(monto)
            if monto_validado:
                desc = input("Descripcion:")
                categoria = input("Categoria:")
                t = Transaccion(monto_validado, desc, categoria, "Ingreso")
                mi_cuenta.agregar_transaccion(t)
        elif opcion_valida == 2 :
            monto = input("Ingrese el monto a gastar:" + "\n")
            monto_validado = validar_numero(monto)
            if monto_validado:
                desc = input("Descripcion:")
                categoria = input("Categoria:")
                t = Transaccion(monto_validado, desc, categoria, "Gasto")
                mi_cuenta.agregar_transaccion(t)
        elif opcion_valida == 3 :
            balance = mi_cuenta.calcular_balance()
            print(f"Balance: {balance}")
            valor_dolar_blue = obtener_dolar_blue()
            if valor_dolar_blue:
                print(f"Valor del dólar blue: {valor_dolar_blue}")
        elif opcion_valida == 4:
            break
        else:
            print("El numero ingresado no es una opcion")
    else:
        print("El valor ingresado no es un numero")