#Laboratorio 4.3.1.7
#Elaborado por: Emmanuel López García
#Fecha: 24 de junio del 2022

def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
# Tu código del LABORATORIO 4.3.6.
#

def days_in_month(year, month):

    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_year_leap(year):
        if months[month - 1] == 28:
            return 29
        else:
            return months[month - 1]
    else:
        return months[month - 1]
    return None
#
# Escribe tu código aquí.
#

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
