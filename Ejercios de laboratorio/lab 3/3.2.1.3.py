'''
Antonio Uribe 
Lab 3.2.1.3
16/10/23
'''
secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

user_number = int(input("Ingresa un número:"))

while user_number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    user_number = int(input("Ingresa un número nuevamente:"))

print("¡Bien hecho, muggle! Eres libre ahora")
