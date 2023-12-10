user_prompt = input('Please enter your name: ')

with open('invitado.txt', 'w) as file:
	file.write(user_prompt)

