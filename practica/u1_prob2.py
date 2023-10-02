'''
Nombre: Antonio Uribe Ramirez
Practica: practica 1
Fecha: 02/10/23
'''
matrias = (
    "Administración de servidores I",
    "Electrónica para IDC Física",
    "Ingles IV",
    "Programación de Redes",
    "Conexión de redes WAN",
    "Probabilidad y Estadística"
)
calificacion = ()
for matrias in matrias:
    calificacion = float(input(f"Introduzca la calificacion de  {matrias}: "))
    calificacion[matrias] = calificacion
for matrias in calificacion: 
    calificacion = calificacion[matrias]  
    print(f"En {matrias} has sacado {calificacion}")

