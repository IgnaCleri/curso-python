def validar_numero(numero):
    try:
        numero = float(numero)
        return numero
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        return None
