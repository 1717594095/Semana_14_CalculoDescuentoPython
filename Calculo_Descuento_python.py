# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el descuento
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

# Primera llamada: solo se proporciona el monto total (se usa el descuento predeterminado de 10%)
monto_total_1 = 700  # Monto total de la primera compra
descuento_1 = calcular_descuento(monto_total_1)
monto_final_1 = monto_total_1 - descuento_1

# Segunda llamada: se proporciona tanto el monto total como el porcentaje de descuento
monto_total_2 = 1600  # Monto total de la segunda compra
porcentaje_descuento_2 = 20  # Porcentaje de descuento personalizado
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
monto_final_2 = monto_total_2 - descuento_2

# Mostrar los resultados de las dos llamadas
print(f"""
Primera compra:
Monto total: ${monto_total_1}
Descuento aplicado: ${descuento_1:.2f}
Monto final a pagar: ${monto_final_1:.2f}

Segunda compra:
Monto total: ${monto_total_2}
Porcentaje de descuento: {porcentaje_descuento_2}%
Descuento aplicado: ${descuento_2:.2f}
Monto final a pagar: ${monto_final_2:.2f}
""")
