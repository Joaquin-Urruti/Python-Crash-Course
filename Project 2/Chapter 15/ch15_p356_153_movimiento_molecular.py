import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
	rw = RandomWalk(num_points=5_000)

	rw.fill_walk()

	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(15, 9))
	point_numbers = range(rw.num_points)
	ax.plot(rw.x_values, rw.y_values, linewidth=0.5)
	ax.set_aspect('equal')

	ax.scatter(0, 0, c='green', s=100, edgecolors='none')
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100, edgecolors='none')
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)
	plt.show()

	keep_running = input("Hacer otro random_walk? (y/n): ")
	if keep_running == 'n':
		break