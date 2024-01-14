import matplotlib.pyplot as plt

x_values = range(0, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

sc = ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, marker='o', edgecolors='none', s=5)

plt.show()
