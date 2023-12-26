# Python program to check if the input number is odd or even. A number is even if 
# division by 2 gives a remainder of 0, if the remainder is 1, it is an odd number.

import os

def get_number():
	number = input('Ingrese un número entero positivo: ')
	return number


def even_odd(number):
	try:
		number = int(number)
		if (number % 2) == 0:
			print(f'El número {number} es par')
		else:
			print(f'El número {number} es impar')
	except:
		print('Entrada no válida')
	leave = input('¿Desea continuar? (S / N): ').lower()
	if leave == 's':
		main()
	else:
		os._exit(0)


def main():
	number = get_number()
	even_odd(number)


main()