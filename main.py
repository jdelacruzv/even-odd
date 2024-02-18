# NOTA: A number is even if division by 2 gives a remainder of 0, if the remainder is 1, it is an odd number.

import os


def leave_sys():
	while True:
		leave = input('¿Desea continuar? (S / N): ').lower()
		if leave == 's':
			main()
		elif leave == 'n':
			os._exit(0)
		else:
			print('Entrada no válida')


def get_number():
	number = input('Ingrese un número entero: ')
	return number


def even_odd(number):
	try:
		number = int(number)
		if (number % 2) == 0:
			print(f'El {number} es par')
		else:
			print(f'El {number} es impar')
	except:
		print('Entrada no válida')
	leave_sys()


def main():
	number = get_number()
	even_odd(number)


main()