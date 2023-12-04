age = 6

if age < 2:
	message = 'You are a baby'
elif age < 4:
	message = 'You are an infant'
elif age < 13:
	message = 'You are a child'
elif age < 20:
	message = 'You are a teenager'
elif age < 65:
	message = 'You are an adult'
else:
	message = 'You are an old man'

print(message)