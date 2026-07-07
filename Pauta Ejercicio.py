"""
Sistema de gestión de ventas - Versión con saltos de línea ordenados
"""

# 1. ENTRADA DE DATOS
# --------------------

nombre_producto = input("Ingresa el nombre del producto: ")

precio_base = float(
    input("Ingresa el precio base del producto en pesos chilenos: ")
)

distancia_km = float(
    input("Ingresa la distancia de envío en kilómetros: ")
)

# 2. CÁLCULOS DE PRECIOS
# ----------------------

porcentaje_iva = 0.19
valor_por_km = 1000

iva = precio_base * porcentaje_iva

if distancia_km < 1:
    costo_envio = 0
else:
    costo_envio = distancia_km * valor_por_km

precio_final = precio_base + iva + costo_envio

# 3. FUNCIÓN PARA FORMATEAR MONTOS
# --------------------------------

def formatear_pesos(monto):
    texto = f"{monto:,.2f}"
    texto = texto.replace(",", "_")
    texto = texto.replace(".", ",")
    texto = texto.replace("_", ".")
    return f"$ {texto}"

# 4. RESUMEN DE LA COMPRA
# -----------------------

print("\n========= RESUMEN DE LA COMPRA =========")
print(f"Producto       : {nombre_producto}")
print(f"Precio base    : {formatear_pesos(precio_base)}")
print(f"Monto de IVA   : {formatear_pesos(iva)}")
print(f"Costo de envío : {formatear_pesos(costo_envio)}")
print(f"Precio final   : {formatear_pesos(precio_final)}")

# 5. MENSAJE FINAL
# ----------------

print("\n------------- DETALLE FINAL -------------")

if distancia_km < 1:
    print("✅ El envío es gratis porque la distancia es menor a 1 km.")
else:
    print("🚚 El envío tiene costo porque la distancia es igual o mayor a 1 km.")

total_recargos = iva + costo_envio
print(
    f"Total de impuestos y recargos (IVA + envío): {formatear_pesos(total_recargos)}"
)

print("\nGracias por usar el sistema de gestión de ventas.")
