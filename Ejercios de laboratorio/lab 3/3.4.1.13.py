'''
Antonio Uribe 
Lab 3.6.1.13
16/10/23
'''
Beatles = []
print("Paso 1:", Beatles)

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

for _ in range(2):
    nuevo_miembro = input("Agrega un miembro de la banda: ")
    Beatles.append(nuevo_miembro)
print("Paso 3:", Beatles)

del Beatles[3:5]
print("Paso 4:", Beatles)

Beatles.insert(0, "Ringo Starr")
print("Paso 5:", Beatles)

print("La longitud de la lista Beatles es:", len(Beatles))

