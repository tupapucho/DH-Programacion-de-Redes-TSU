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


#Segundo ejercico 
def leer_valor(mensaje):
    try:
        valor = float(input(mensaje))
        return valor
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return leer_valor(mensaje)

a = leer_valor("Ingresa el coeficiente a: ")
b = leer_valor("Ingresa el coeficiente b: ")
c = leer_valor("Ingresa el coeficiente c: ")

discriminante = b**2 - 4*a*c

if discriminante >= 0:
    x1 = (-b + discriminante**0.5) / (2*a)
    x2 = (-b - discriminante**0.5) / (2*a)
    print("X1 =", x1)
    print("X2 =", x2)
else:
    print("La ecuación no tiene soluciones reales.")
