
a = float(input("Ingresa el coeficiente 'a': "))
b = float(input("Ingresa el coeficiente 'b': "))
c = float(input("Ingresa el coeficiente 'c': "))

discriminante = b**2 - 4*a*c

if discriminante >= 0:
    x1 = (-b + discriminante**0.5) / (2*a)
    x2 = (-b - discriminante**0.5) / (2*a)
    print(f"X1 = {x1}")
    print(f"X2 = {x2}")
else:
    print("La ecuación no tiene raíces reales.")

