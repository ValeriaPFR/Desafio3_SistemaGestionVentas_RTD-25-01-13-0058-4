"""
Desafío: Sistema de Gestión de Venta de Productos-Desafío Latam
Empresa: ESPIRALIA SpA
Autor: Valeria Fariña R.
"""
# =====================================================================
# 1. ENTRADA DE DATOS
# =====================================================================
# Solicitamos los datos al usuario mediante mensajes claros y descriptivos.

# Convertimos los datos numéricos al tipo float para admitir decimales.

nombre_producto = input("Ingrese el nombre del producto: ")

precio_base = float(
    input("Ingrese el precio base del producto (en CLP): ")
)

distancia_envio_km = float(
    input("Ingrese la distancia de envío en kilómetros (km): ")
)
# =====================================================================
# 2. CÁLCULOS DE PRECIOS
# =====================================================================
# Definimos constantes y realizamos las operaciones aritméticas requeridas.

PORCENTAJE_IVA = 0.19         # Constante para el impuesto del 19%
VALOR_POR_KILOMETRO = 1000    # Costo por kilómetro de transporte ($1.000)

# Calcular el impuesto al valor agregado (IVA)
monto_iva = precio_base * PORCENTAJE_IVA

# Calcular el costo de envío basándose en la distancia condicional
if distancia_envio_km < 1:
    costo_envio = 0.0         # El envío es gratis si es menor a 1 km
else:
    costo_envio = distancia_envio_km * VALOR_POR_KILOMETRO

# Calcular la sumatoria del precio final estructurado
precio_final = precio_base + monto_iva + costo_envio

# Calcular el total acumulado de cargas impositivas y de transporte
total_impuestos_recargos = monto_iva + costo_envio
# =====================================================================
# 3. FUNCIÓN DE FORMATEO PARA PESOS CHILENOS
# =====================================================================
# Esta función asegura que los montos se muestren en formato CLP ($ X.XXX,XX)
# utilizando f-strings y reemplazando los separadores según la convención local.

def formatear_clp(monto):
    # Formatear inicialmente con f-string a 2 decimales y comas en miles
    texto_formateado = f"{monto:,.2f}"
    # Intercambiar los separadores anglosajones por los chilenos (puntos en miles, coma en decimal)
    texto_formateado = texto_formateado.replace(",", "_").replace(".", ",").replace("_", ".")
    return f"$ {texto_formateado}"
# =====================================================================
# 4. PRESENTACIÓN DE RESULTADOS
# =====================================================================
# Desplegamos el resumen estructurado alineando los textos de forma limpia.
print("\n========================================")
print("          RESUMEN DE LA COMPRA          ")
print("========================================")
print(f"Nombre del producto : {nombre_producto}")
print(f"Precio base         : {formatear_clp(precio_base)}")
print(f"Monto de IVA (19%)  : {formatear_clp(monto_iva)}")
print(f"Costo de envío      : {formatear_clp(costo_envio)}")
print("----------------------------------------")
print(f"PRECIO FINAL        : {formatear_clp(precio_final)}")
print("========================================")
# =====================================================================
# 5. MENSAJE FINAL
# =====================================================================
# Evaluamos e informamos de forma profesional las condiciones finales de envío y cobros.
print("\n--- DETALLES DE DESPACHO E IMPUESTOS ---")
if distancia_envio_km < 1:
    print("✅ ¡Felicitaciones! Su envío es gratis debido a que la distancia es menor a 1 km.")
else:
    print("🚚 El despacho tiene costo asociado por ser una distancia igual o mayor a 1 km.")
print(f"Total de impuestos y recargos acumulados (IVA + envío): {formatear_clp(total_impuestos_recargos)}")
print("--------------------------------------------------------")
print("Gracias por preferir nuestro sistema de gestión de ventas.\n")