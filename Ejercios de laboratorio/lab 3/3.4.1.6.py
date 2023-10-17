'''
Antonio Uribe 
Lab 3.6.1.6
16/10/23
'''

hat_list = [1, 2, 3, 4, 5]

numero_usuario = int(input("Ingresa un número entero para reemplazar el número del medio: "))
hat_list[2] = numero_usuario

hat_list.pop()

print("La longitud de la lista es:", len(hat_list))
print(hat_list)
