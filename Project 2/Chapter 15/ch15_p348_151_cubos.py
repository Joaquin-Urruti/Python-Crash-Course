import matplotlib.pyplot as plt

x_values = range(0,5001)

y_values = [x**3 for x in x_values]


plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(x_values, y_values)

plt.show()
