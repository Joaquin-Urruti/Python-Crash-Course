motorcycles = ['honda', 'yamaha', 'susuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'susuki']

# Append adds a new element at the end of a list
motorcycles.append('ducati')
print(motorcycles)

# Insert adds a new elemnt in the selected position
motorcycles.insert(0, 'kawasaki')
print(motorcycles)

# Del deletes an elemnt if the position is known and the value can't be used after deletion
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Pop deletes the las element if we don't pass any position
# It's used when we want to use the value being deleted from a list
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Pops second element on the list and  assigns it to second_motorcycle variable
motorcycles = ['kawasaki', 'honda', 'yamaha', 'susuki', 'ducati']
second_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(second_motorcycle)

# Removes the first time an element appears in a list, by it's value
motorcycles.remove('susuki')
print(motorcycles)




