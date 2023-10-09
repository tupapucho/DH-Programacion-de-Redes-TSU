'''
Nombre alumno: Antonio uribe 
Pratica parcial
asignatura: Programación de Redes
fecha: 09/10/23
'''
datos = []
for i in range(5):
    dato = int(input("Ingrese un número entero: "))
    datos.append(dato)

tuplaDatos = tuple(datos)

def mostrar_tupla(tupla):
    for elemento in tupla:
        print(elemento)

mostrar_tupla(tuplaDatos)

print("La longitud de la tupla es:", len(tuplaDatos))

def sumar_tupla(tupla):
    total = sum(tupla)
    return total

resultado = sumar_tupla(tuplaDatos)
print("La suma de los elementos en la tupla es:", resultado)

resultado = sumar_tupla(tuplaDatos)
print("La suma de los elementos en la tupla es:", resultado)

tuplaDatos = tuplaDatos[:-1] + (tuplaDatos[-1] * 2,)

print("Contenido de la tupla después del reemplazo:")
mostrar_tupla(tuplaDatos)

def multiplica_tupla(tupla):
    total = 1
    for elemento in tupla:
        total *= elemento
    return total

resultado_multiplicacion = multiplica_tupla(tuplaDatos)
print("El resultado de la multiplicación de los elementos en la tupla es:", resultado_multiplicacion)


