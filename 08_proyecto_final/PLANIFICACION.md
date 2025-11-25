# Registro de Cambios - Proyecto Organización Facu

## [2025-11-25] Mejora en obtención de Dólar Blue

### Descripción
Se mejoró la robustez de la función `obtener_dolar_blue` en `utils.py` al migrar a una API más estable (`dolarapi.com`) e implementar manejo de errores y timeouts.

### Detalles Técnicos
- **Archivo modificado**: `utils.py`
- **Cambios**:
    - Se cambió el endpoint a `https://dolarapi.com/v1/dolares/blue`.
    - Se agregó `timeout=5` a la petición `requests.get` para evitar bloqueos indefinidos.
    - Se implementó `response.raise_for_status()` para detectar errores HTTP (4xx, 5xx).
    - Se agregó captura específica de `requests.exceptions.RequestException` para errores de conexión.
- **Pruebas**:
    - Se agregó un caso de prueba en `test_proyecto.py` que verifica la obtención correcta del valor del dólar o maneja el error de red sin romper la ejecución.
