current_users = ['Joaquin', 'Juan', 'Rodrigo', 'Pedro', 'Lautaro']

current_users = [user.lower() for user in current_users]


new_users = ['José', 'Javier', 'Jorge', 'joaquin', 'Manuel']

for user in new_users:
	if user.lower() not in current_users:
		print('Your selected user is ok')
	else:
		print(f'The user: {user} has already been taken')
