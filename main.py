#def dog(func):
#	def wrapper():
#		func()
#		print('у него есть злая собака ')
#	return wrapper

#def angry(func):
#	def wrapper():
#		func()
#		print('он злой')
#	return wrapper

#def morning(func):
#	def wrapper():
#		func()
#		print('по утрам он злобно варт себе кофе')
#	return wrapper

#def Work(func):
#	def wrapper():
#		func()
#		print('у него есть работа где он злой злитса на клиентов')
#	return wrapper

#def car(func):
#	def wrapper():
#		func()
#		print('у злого человека есть машина и он постоянно злитса ведь его машина постоянно ломаетса')
#	return wrapper

#def house(func):
#	def wrapper():
#		func()
#		print('у него есть старый дом  и человек злитса что его дом старый')
#	return wrapper

#def computer(func):
#	def wrapper():
#		func()
#		print('у него есть компютер и он постоянно злитса что на его клавиотуре постоянно заедает буква Ч')
#	return wrapper

#def atolation(func):
#	def wrapper():
#		func()
#		print('злой человек всегда платит за отопление и злитса когда ему зимой его отключают')
#	return wrapper

#def neighbours(func):
#	def wrapper():
#		func()
#		print('злой человек постоянно злитса на своих соседей так как они щастливы а он постоянно злой')
#	return wrapper

#def happiness(func):
#	def wrapper():
#		func()
#		print('но в свой день рождения злой человек щастлив ведь его день рождения в пятницу 13того и все вокруг него не щатливы а он щастлив')
#	return wrapper
    
#@happiness
#@neighbours
#@atolation
#@computer
#@house
#@car   
#@Work
#@morning
#@dog
#@angry

#def human():
#	print('это человек')

#human()


num1 = num2 = sign = ''
while num1 == '' or num2 == '' or sign == '':
	try:
		num1 = int(input('Number1: '))
		sign = input('Sign: ')
		num2 = int(input('Number2: '))
		if sign == '/' and num2 == 0:
			raise ZeroDivisionError
	except ValueError:
		print('Wrong value')
	except ZeroDivisionError:
		sign = ''
		print('Go to school')
	except:
		print('Something go wrong')	try:
		if sign == '+':
			print(f"{num1} + {num2} = {num1+num2}")
	except TypeError:
		print('Wrong types')
	try:
		if sign == '-':
			print(f"{num1} - {num2} = {num1-num2}")
	except TypeError:
		print('Wrong types')
	try:
		if sign == '*':
			print(f"{num1} * {num2} = {num1*num2}")
	except TypeError:
		print('Wrong types')
	try:
		if sign == '/':
			print(f"{num1} / {num2} = {num1/num2}")
	except TypeError:
		print('Wrong types')
	try:
		if sign != "-" or sign!="+" or sign!="/" or sign!="*":
			raise TypeError
	except TypeError:
           print("нет такого знака в матиматике")