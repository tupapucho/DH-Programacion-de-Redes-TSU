'''
Antonio Uribe 
Lab 3.1.1.11
16/10/23
'''
year = int(input("Introduce un año:"))

if year >= 1582:
    if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
        print("Año Común")
    else:
        print("Año Bisiesto")
else:
    print("No está dentro del período del calendario Gregoriano")
