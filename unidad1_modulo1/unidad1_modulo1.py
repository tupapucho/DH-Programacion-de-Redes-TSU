'''
Nombre: Antonio Uribe Ramirez
Practica: Evaluacion 
Fecha: 25/09/23
'''

#Primer ejercicio panaderia 
precio_de_pieza = 3.49
descuento = 0.60
pan_no_fresco = int(input("cuantas piezas de pan no fresco son: "))
costo_total = pan_no_fresco * precio_de_pieza* (1 - descuento)
print(f"Precio habitual por barra de pan: ${precio_de_pieza:.2f}")
print(f"Descuento por por pan no fresco: ({descuento * 100}%): ${precio_de_pieza * descuento:.2f}")
print(f"Costo total de las barras de pan: ${costo_total:.2f}")


