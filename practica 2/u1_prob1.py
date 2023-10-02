'''
Nombre: Antonio Uribe Ramirez
Practica: ejercicio1
Fecha: 02/10/23
'''
monto_inicial = float(input("Ingrese la cantidad de dinero depositada en la cuenta de ahorros: "))
monto_1_year = round(monto_inicial * 1.04, 2)
monto_2_year = round(monto_1_year * 1.04, 2)
monto_3_year = round(monto_2_year * 1.04, 2)
print(f"Ahorros después del primer año: {monto_1_year}")
print(f"Ahorros después del segundo año: {monto_2_year}")
print(f"Ahorros después del tercer año: {monto_3_year}")
