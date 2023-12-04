guests = ['Miles Davis', 'Roy Hargrove', 'Tom Harrell' ,'Santiago Bilinkis', 'Max Tegmark']
print(guests)

absent = 'Max Tegmark'
guests.remove(absent)

replacement = 'Bill Evans'
guests.append(replacement)
print(guests)

print(f'Would you like to come to dinner {guests[0]}?')
print(f'Would you like to come to dinner {guests[1]}?')
print(f'Would you like to come to dinner {guests[2]}?')
print(f'Would you like to come to dinner {guests[3]}?')
print(f'Would you like to come to dinner {guests[4]}?')