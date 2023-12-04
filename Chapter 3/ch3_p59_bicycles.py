bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# print the list
print(bicycles)

# print first element of the list
print(bicycles[0])

# print the second element on the list with title style
print(bicycles[1].title())

# print the last element of the list in capitals
print(bicycles[-1].upper())

# print message using position in the list
message = f'My first bike was a {bicycles[-2].title()}'
print(message)