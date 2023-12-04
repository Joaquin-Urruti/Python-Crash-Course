juan = {'nombre':'Juan', 'apellido':'Perez', 'ciudad':'Azul'}
pedro = {'nombre':'Pedro', 'apellido':'Gonzalez', 'ciudad':'Olavarría'}
ernesto = {'nombre':'Ernesto', 'apellido':'Jodos', 'ciudad':'Buenos Aires'}

personas = [juan, pedro, ernesto]

print(juan)

for persona in personas:
	for k, v in persona.items():
		nombre = persona.get('nombre')
		apellido = persona.get('apellido')
		ciudad = persona.get('ciudad')

		print(f'{nombre.title()} {apellido.title()} vive en la ciudad de {ciudad.title()}.')