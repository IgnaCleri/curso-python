import requests
def validar_numero(numero):
    try:
        numero = float(numero)
        return numero
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        return None

def obtener_dolar_blue():
    try:
        response = requests.get("https://dolarapi.com/v1/dolares/blue", timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["venta"]
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None
    except Exception as e:
        print(f"Error al obtener el valor del dólar blue: {e}")
        return None
