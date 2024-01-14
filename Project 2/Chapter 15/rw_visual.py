import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(num_points=100_000)

rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()