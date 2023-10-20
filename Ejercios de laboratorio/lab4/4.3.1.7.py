﻿'''
Autor: Antonio Uribe Ramirez 
Fecha 19/10/23
Descripcion: Laboratorio 4.3.1.7
'''
def is_year_leap(year):
#
# Tu código del LABORATORIO 4.3.1.6
#
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
#
# Escribe tu código aquí.
#
    days_por_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        days_por_month[2] = 29

    if month < 1 or month > 12:
        return None
    return days_por_month[month]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")

