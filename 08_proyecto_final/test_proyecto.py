from models import Transaccion, Cuenta
from utils import validar_numero

def probar_proyecto():
    print("--- Iniciando Pruebas del Gestor de Finanzas ---")

    # 1. Prueba de Utils
    print("\n1. Probando validaciones (utils.py)...")
    num = validar_numero("100.50")
    if num == 100.50:
        print("✅ Validación de número correcta.")
    else:
        print("❌ Error en validación de número.")
    
    error = validar_numero("texto")
    if error is None:
        print("✅ Validación de texto correcta (retornó None).")
    else:
        print("❌ Error: Debería retornar None para texto.")

    print("\nProbando obtener_dolar_blue (utils.py)...")
    from utils import obtener_dolar_blue
    dolar = obtener_dolar_blue()
    if dolar:
        print(f"✅ Dólar Blue obtenido: {dolar}")
    else:
        print("⚠️ No se pudo obtener el Dólar Blue (puede ser error de red).")

    # 2. Prueba de Modelos
    print("\n2. Probando Modelos (models.py)...")
    mi_cuenta = Cuenta()
    
    # Agregar Ingreso
    t1 = Transaccion(1000, "Sueldo", "Trabajo", "Ingreso")
    mi_cuenta.agregar_transaccion(t1)
    print(f"Agregada: {t1}")

    # Agregar Gasto
    t2 = Transaccion(200, "Compra", "Super", "Gasto")
    mi_cuenta.agregar_transaccion(t2)
    print(f"Agregada: {t2}")

    # Verificar Balance
    balance = mi_cuenta.calcular_balance()
    esperado = 800
    
    if balance == esperado:
        print(f"✅ Balance calculado correctamente: {balance}")
    else:
        print(f"❌ Error en balance. Esperado: {esperado}, Obtenido: {balance}")

    print("\n--- Fin de las pruebas ---")

if __name__ == "__main__":
    probar_proyecto()
