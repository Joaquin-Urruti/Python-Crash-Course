auto = input('Qué modelo de auto desea alquilar?')

if ' ' in auto:
	marca = auto.split(' ')[-1].title()
	prefijo = auto.split(' ')[0]
	print(f'Veamos si tenemos {prefijo} {marca} para usted.')
else:
	print(f'Veamos si tenemos un {auto} para usted.')